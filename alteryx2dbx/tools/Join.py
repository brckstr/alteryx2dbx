import json
from ..node import AlteryxNode

class Join(AlteryxNode):
    description = ("The Join tool allows you to combine two datasets on a set of join conditions")
    caveats = ("")

    def __init__(self, node_dict, environment):
        super().__init__(node_dict, environment)

    def render_code(self):
        # add connections to join_options
        self.node_dict["join_options"]["left"] = self.inputs["Left"]
        self.node_dict["join_options"]["right"] = self.inputs["Right"]
        return self.template.render({
            "node":self.node_dict, 
            "id": self.node_dict["@ToolID"], 
            "tool": self.tool_dict,
            "output_name": self.output_name,
            "join_options": self.node_dict["join_options"]
        })

    @staticmethod
    def modify_dict(node_dict):
        join_fields = { "Left": [], "Right": []}
        select_fields = []
        star = False
        for field_side in node_dict["Properties"]["Configuration"]["JoinInfo"]:
            for field in field_side["Field"]:
                join_fields[field_side["@connection"]].append(field["@field"])
        field_obj = node_dict["Properties"]["Configuration"]["SelectConfiguration"]["Configuration"]["SelectFields"]["SelectField"]
        if isinstance(field_obj,dict):
            field_obj = [field_obj]
        for field in field_obj:
            # if field["@selected"] == "True":
            if field["@field"] == "*Unknown":
                star = True
            else:
                side, *fname = field["@field"].split("_")
                select_fields.append(("%s.%s" % (side, "_".join(fname)),field.get("@rename",field["@field"])))
        node_dict["join_options"] = {
            "select_fields": select_fields,
            "conditions": list(zip(join_fields["Left"], join_fields["Right"])),
            "star": star,
            "type": "left"
        }
        return node_dict
