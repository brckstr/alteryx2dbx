from ..node import AlteryxNode

class ToolContainer(AlteryxNode):
    description = ("The ToolContainer tool groups tools together")
    caveats = ("")

    def __init__(self, node_dict, environment):
        super().__init__(node_dict, environment)

    def render_code(self):
        return self.template.render({
            "node":self.node_dict, 
            "id": self.node_dict["@ToolID"], 
            "tool": self.tool_dict,
            "node_ids": self.node_dict["child_nodes"]
        })

    @classmethod
    def modify_dict(cls, node_dict):
        node_dict["child_nodes"] = [field["@ToolID"] for field in cls.list_items(node_dict["ChildNodes"]["Node"])]
        return node_dict