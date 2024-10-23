import json
from ..node import AlteryxNode

class InputData(AlteryxNode):
    description = ("Databricks has a number of source connectors for different types of files and source data systems. "
    "This tool does its best to detect the file or connector type and plug in the appropriate code, but some modifications "
    "will be required.")
    caveats = ("Databricks does not have access to your local file system, so any files that you wish to process will first "
        "need to be uploaded to the platform. Upload files to a volume in order to access them.")

    def __init__(self, node_dict, environment):
        super().__init__(node_dict, environment)

    def render_code(self):
        return self.template.render({"node":self.node_dict, "conns": self.connections, "id": self.node_dict["@ToolID"], "tool": self.tool_dict, "node_dict": "# "+"\n# ".join(json.dumps(self.node_dict, indent=4).split("\n"))})

    @staticmethod
    def modify_dict(node_dict):
        return node_dict
