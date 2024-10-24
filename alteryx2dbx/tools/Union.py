import json
from ..node import AlteryxNode

class Union(AlteryxNode):
    description = ("The Union tool allows you to combine two datasets")
    caveats = ("")

    def __init__(self, node_dict, environment):
        super().__init__(node_dict, environment)

    def render_code(self):
        # add connections to join_options
        return self.template.render({
            "node":self.node_dict, 
            "id": self.node_dict["@ToolID"], 
            "tool": self.tool_dict,
            "output_name": self.output_name,
            "inputs": self.inputs["Input"]
        })

    @staticmethod
    def modify_dict(node_dict):
        return node_dict
