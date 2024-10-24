import json
from ..node import AlteryxNode

class Summarize(AlteryxNode):
    description = ("The Summarize tool allows you to perform aggregate calculations over columns in the input dataset")
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
            "input_name": self.inputs["Input"],
            "summarize_options": self.node_dict["summarize_options"]
        })

    @classmethod
    def modify_dict(cls, node_dict):
        groupby_fields = []
        agg_ops = []
        field_obj = node_dict["Properties"]["Configuration"]["SummarizeFields"]["SummarizeField"]
        for field in cls.list_items(field_obj):
            if field["@action"] == "GroupBy":
                groupby_fields.append(field["@field"])
            else:
                agg_ops.append({n.strip("@"):field[n] for n in field})
        node_dict["summarize_options"] = {"groupby_fields": groupby_fields, "agg_ops": agg_ops}
        return node_dict
