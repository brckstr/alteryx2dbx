import os
from collections import defaultdict
from xml.etree import cElementTree as ET

from jinja2 import Environment, FileSystemLoader

from .tools import *
from .tool_defs import tool_defs
from .node import AlteryxNode

class AlteryxWorkflow(object):
    """docstring for AlteryxWorkflow"""
    environment = Environment(loader=FileSystemLoader(os.path.join(os.path.dirname(__file__),"templates")))

    def __init__(self, etree_contents):
        self.workflow_dict = self.etree_to_dict(etree_contents)["AlteryxDocument"]
        self.name = self.workflow_dict["Properties"]["MetaInfo"]["Name"]
        self.description = self.workflow_dict["Properties"]["MetaInfo"]["Description"]
        self.node_dict = {}
        for n in self.workflow_dict["Nodes"]["Node"]:
            if n["GuiSettings"]["@Plugin"] == "AlteryxGuiToolkit.ToolContainer.ToolContainer":
                children = n["ChildNodes"]["Node"]
                if not isinstance(children, list):
                    children = [children]
                for c in children:
                    print(c)
                    self.node_dict[c["@ToolID"]] = self.tool_lookup(c)
            self.node_dict[n["@ToolID"]] = self.tool_lookup(n) 
        self.connection_list = self.workflow_dict["Connections"]["Connection"]
        self.import_list = []
        self.template = self.environment.get_template("workflow.txt")
        for conn in self.connection_list:
            self.update_connection(conn)

    @classmethod
    def tool_lookup(cls, node_dict):
    	tool_class = node_dict["GuiSettings"]["@Plugin"]
    	new_node = tool_defs[tool_class] or AlteryxNode
    	return new_node(node_dict, cls.environment)

    @staticmethod
    def etree_to_dict(t):
        d = {t.tag: {} if t.attrib else None}
        children = list(t)
        if children:
            dd = defaultdict(list)
            for dc in map(AlteryxWorkflow.etree_to_dict, children):
                for k, v in dc.items():
                    dd[k].append(v)
            d = {t.tag: {k:v[0] if len(v) == 1 else v for k, v in dd.items()}}
        if t.attrib:
            d[t.tag].update(('@' + k, v) for k, v in t.attrib.items())
        if t.text:
            text = t.text.strip()
            if children or t.attrib:
                if text:
                  d[t.tag]['#text'] = text
            else:
                d[t.tag] = text
        return d

    @classmethod
    def from_string(cls, file_contents):
        e = ET.XML(file_contents)
        return cls(e)

    @classmethod
    def from_file(cls, filepath):
        with open(filepath,"r") as ifile:
            return cls.from_string(ifile.read())

    def update_connection(self, connection):
        input_tool_id = connection["Origin"]["@ToolID"]
        input_value = self.node_dict[input_tool_id].output_name
        output_tool_id = connection["Destination"]["@ToolID"]
        output_key = connection["Destination"]["@Connection"]
        if (current_value:=self.node_dict[output_tool_id].inputs.get(output_key)):
            if isinstance(current_value,list):
                self.node_dict[output_tool_id].inputs[output_key].append(input)
            else:
                self.node_dict[output_tool_id].inputs[output_key] = [current_value, input_value]
        else:
            self.node_dict[output_tool_id].inputs[output_key]= input_value

    def to_string(self):
        node_list = [self.node_dict[str(i)].render_code() for i in sorted(self.node_dict,key=int)]
        rendered_nodes = "\n".join(node_list)
        return self.template.render({"workflow_name":self.name, "workflow_description": self.description, "nodes": rendered_nodes})
