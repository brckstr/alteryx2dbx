import json

from .class_defs import class_defs

class AlteryxNode(object):

	def __init__(self, node_dict, environment):
		self.template = environment.get_template(f"{self.__class__.__name__}.txt")
		self.node_dict = self.modify_dict(node_dict)
		self.connections = {}
		self.tool_dict = class_defs[node_dict["GuiSettings"]["@Plugin"]]
		self.output_name = self.tool_dict["class"].lower() + self.node_dict["@ToolID"]
		self.inputs = {}

	def render_code(self):
		return self.template.render({"node":self.node_dict, "conns": self.connections, "id": self.node_dict["@ToolID"], "tool": self.tool_dict, "node_dict": "# "+"\n# ".join(json.dumps(self.node_dict, indent=4).split("\n"))})

	@staticmethod
	def modify_dict(node_dict):
		return node_dict