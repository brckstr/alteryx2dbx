import json
from ..node import AlteryxNode

class Comment(AlteryxNode):
    description = ("The comment tool allows you to add descriptive text to your workflow")
    caveats = ("In the Alteryx XML code, the Comment tool nodes are not specifically connected to other nodes"
        "and therefore they simply appear in the order of the node list. Efforts may be made in future to reorder"
        "these cells in future based on their proximity in the flow UI.")

    def __init__(self, node_dict, environment):
        super().__init__(node_dict, environment)

    def render_code(self):
        return self.template.render({"node":self.node_dict, "id": self.node_dict["@ToolID"], "tool": self.tool_dict, "comment_text": self.node_dict["comment_text"]})

    @staticmethod
    def modify_dict(node_dict):
        node_dict["comment_text"] = node_dict["Properties"]["Configuration"]["Text"]
        return node_dict