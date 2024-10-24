from ..node import AlteryxNode

class Select(AlteryxNode):
    description = ("The Select tool allows you to select a subset of input columns to return")
    caveats = ("")

    def __init__(self, node_dict, environment):
        super().__init__(node_dict, environment)

    def render_code(self):
        return self.template.render({
            "node":self.node_dict, 
            "id": self.node_dict["@ToolID"], 
            "tool": self.tool_dict,
            "output_name": self.output_name,
            "input_name": self.inputs["Input"],
            "select_expression": self.node_dict["select_expression"]
        })

    @classmethod
    def modify_dict(cls, node_dict):
        fields = []
        field_obj = node_dict["Properties"]["Configuration"]["SelectFields"]["SelectField"]
        for field in cls.list_items(field_obj):
            if field["@selected"] == "True":
                fields.append(field["@field"])
        node_dict["select_expression"] = "\""+"\",\"".join(fields)+"\""
        return node_dict

# <Node ToolID="22">
#   <GuiSettings Plugin="AlteryxBasePluginsGui.AlteryxSelect.AlteryxSelect">
#     <Position x="270" y="90" />
#   </GuiSettings>
#   <Properties>
#     <Configuration>
#       <OrderChanged value="False" />
#       <CommaDecimal value="False" />
#       <SelectFields>
#         <SelectField field="Step" selected="True" type="Int64" size="8" />
#         <SelectField field="*Unknown" selected="True" />
#       </SelectFields>
#     </Configuration>
#     <Annotation DisplayMode="0">
#       <Name />
#       <DefaultAnnotationText />
#       <Left value="False" />
#     </Annotation>
#     <MetaInfo connection="Output">
#       <RecordInfo>
#         <Field name="Worker" source="TextInput:" type="Byte" />
#         <Field name="Task" size="1" source="TextInput:" type="String" />
#         <Field name="Step" source="TextInput:" type="Int64" />
#       </RecordInfo>
#       <SortInfo>
#         <Field field="Worker" order="Asc" />
#       </SortInfo>
#     </MetaInfo>
#   </Properties>
#   <EngineSettings EngineDll="AlteryxBasePluginsEngine.dll" EngineDllEntryPoint="AlteryxSelect" />
# </Node>