import json
from ..node import AlteryxNode

class Sort(AlteryxNode):
    description = ("The comment tool allows you to add descriptive text to your workflow")
    caveats = ("In the Alteryx XML code, the Comment tool nodes are not specifically connected to other nodes"
        "and therefore they simply appear in the order of the node list. Efforts may be made in future to reorder"
        "these cells in future based on their proximity in the flow UI.")

    def __init__(self, node_dict, environment):
        super().__init__(node_dict, environment)

    def render_code(self):
        return self.template.render({
            "node":self.node_dict, 
            "id": self.node_dict["@ToolID"], 
            "tool": self.tool_dict,
            "output_name": self.output_name,
            "input_name": self.inputs["Input"],
            "sort_options": self.node_dict["sort_options"]
        })

    @classmethod
    def modify_dict(cls, node_dict):
        fields = []
        orders = []
        field_obj = node_dict["Properties"]["Configuration"]["SortInfo"]["Field"]
        for field in cls.list_items(field_obj):
            fields.append(field["@field"])
            orders.append(field["@order"] == "Ascending")
        node_dict["sort_options"] = {"fields": fields, "orders": orders} # )+"\", ascending=[" +",".join(orders) +"]"
        return node_dict

# Add Annotation text