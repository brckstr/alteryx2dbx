import json
import re
from ..node import AlteryxNode

class InputData(AlteryxNode):
    description = ("Databricks has a number of source connectors for different types of files and source data systems. "
    "This tool does its best to detect the file or connector type and plug in the appropriate code, but some modifications "
    "will be required.")
    caveats = ("Databricks does not have access to your local file system, so any files that you wish to process will first "
        "need to be uploaded to the platform. Upload files to a volume in order to access them.")
    match_patterns = {
        "oracle": r'oci:(?P<username>[^\/]+)\/(?P<password>[^@]+)\@(?P<jdbc_url>(?P<hostname>[^:\/]+)(:(?P<port>\d+))?/(?P<database>\w+))'
    }

    def __init__(self, node_dict, environment):
        super().__init__(node_dict, environment)

    def render_code(self):
        return self.template.render({
            "node":self.node_dict, 
            "conns": self.connections, 
            "id": self.node_dict["@ToolID"], 
            "tool": self.tool_dict, 
            "output_name": self.output_name,
            "node_dict": "# "+"\n# ".join(json.dumps(self.node_dict, indent=4).split("\n")),
            "file_type": self.node_dict["file_type"],
            "file_opts": self.node_dict["file_opts"]
        })

    @classmethod
    def modify_dict(cls, node_dict):
        file_opts = {}
        if node_dict["Properties"]["Configuration"]["File"]["#text"].startswith("oci"):
            node_dict["file_type"] = "oracle"
            conn_components, query = node_dict["Properties"]["Configuration"]["File"]["#text"].split("|||")
            file_opts["query"] = "\n        ".join(query.split("\n"))
            match = re.search(cls.match_patterns["oracle"], conn_components)
            if match:
                file_opts["username"] = match["username"]
                file_opts["jdbc_url"] = match["jdbc_url"]
        else:
            node_dict["file_type"] = "Unknown"
        node_dict["file_opts"] = file_opts
        return node_dict

