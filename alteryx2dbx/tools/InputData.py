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

# <Node ToolID="1">
#   <GuiSettings Plugin="AlteryxBasePluginsGui.DbFileInput.DbFileInput">
#     <Position x="54" y="102" />
#   </GuiSettings>
#   <Properties>
#     <Configuration>
#       <Passwords>48A25A514F19B46366AABA13623EF08547DD6B3C8</Passwords>
#       <File RecordLimit="" FileFormat="17">oci:RMOR_PROD/__EncPwd1__@LOADING.DATAWAREHOUSE.DB.INSIDEAAG.COM:1522/EDWPROD|||SELECT *



# FROM



# APP_RMINV.ART_GC_RULES GC



# WHERE GC.SNAPSHOT_DATE BETWEEN TRUNC(SYSDATE)-7 AND TRUNC(SYSDATE)</File>
#       <FormatSpecificOptions>
#         <PreSQLOnConfig>True</PreSQLOnConfig>
#         <ReadCentroids>False</ReadCentroids>
#         <TableStyle>Quoted</TableStyle>
#         <NoProgress>False</NoProgress>
#         <CacheData>False</CacheData>
#         <PostSQL />
#         <PreSQL />
#         <ForceSqlWcharSupport>False</ForceSqlWcharSupport>
#       </FormatSpecificOptions>
#     </Configuration>
#     <Annotation DisplayMode="0">
#       <Name><![CDATA[GC ]]></Name>
#       <DefaultAnnotationText><![CDATA[GC ]]></DefaultAnnotationText>
#       <Left value="False" />
#     </Annotation>
#     <MetaInfo connection="Output">
#       <RecordInfo>
#         <Field name="SNAPSHOT_DATE" source="File: oci:RMOR_PROD/__EncPwd1__@LOADING.DATAWAREHOUSE.DB.INSIDEAAG.COM:1522/EDWPROD|||SELECT *&#xA;&#xA; &#xA;&#xA;FROM&#xA;&#xA; &#xA;&#xA;APP_RMINV.ART_GC_RULES GC&#xA;&#xA; &#xA;&#xA;WHERE GC.SNAPSHOT_DATE BETWEEN TRUNC(SYSDATE)-7 AND TRUNC(SYSDATE)" type="DateTime" />
#         <Field name="NDOD" size="48" source="File: oci:RMOR_PROD/__EncPwd1__@LOADING.DATAWAREHOUSE.DB.INSIDEAAG.COM:1522/EDWPROD|||SELECT *&#xA;&#xA; &#xA;&#xA;FROM&#xA;&#xA; &#xA;&#xA;APP_RMINV.ART_GC_RULES GC&#xA;&#xA; &#xA;&#xA;WHERE GC.SNAPSHOT_DATE BETWEEN TRUNC(SYSDATE)-7 AND TRUNC(SYSDATE)" type="V_String" />
#         <Field name="OD" size="48" source="File: oci:RMOR_PROD/__EncPwd1__@LOADING.DATAWAREHOUSE.DB.INSIDEAAG.COM:1522/EDWPROD|||SELECT *&#xA;&#xA; &#xA;&#xA;FROM&#xA;&#xA; &#xA;&#xA;APP_RMINV.ART_GC_RULES GC&#xA;&#xA; &#xA;&#xA;WHERE GC.SNAPSHOT_DATE BETWEEN TRUNC(SYSDATE)-7 AND TRUNC(SYSDATE)" type="V_String" />
#         <Field name="YIELD_USER_ID" size="25" source="File: oci:RMOR_PROD/__EncPwd1__@LOADING.DATAWAREHOUSE.DB.INSIDEAAG.COM:1522/EDWPROD|||SELECT *&#xA;&#xA; &#xA;&#xA;FROM&#xA;&#xA; &#xA;&#xA;APP_RMINV.ART_GC_RULES GC&#xA;&#xA; &#xA;&#xA;WHERE GC.SNAPSHOT_DATE BETWEEN TRUNC(SYSDATE)-7 AND TRUNC(SYSDATE)" type="String" />
#         <Field name="PLNG_REG_SHORT_NAME" size="15" source="File: oci:RMOR_PROD/__EncPwd1__@LOADING.DATAWAREHOUSE.DB.INSIDEAAG.COM:1522/EDWPROD|||SELECT *&#xA;&#xA; &#xA;&#xA;FROM&#xA;&#xA; &#xA;&#xA;APP_RMINV.ART_GC_RULES GC&#xA;&#xA; &#xA;&#xA;WHERE GC.SNAPSHOT_DATE BETWEEN TRUNC(SYSDATE)-7 AND TRUNC(SYSDATE)" type="String" />
#         <Field name="DIRECTION_IND" size="1" source="File: oci:RMOR_PROD/__EncPwd1__@LOADING.DATAWAREHOUSE.DB.INSIDEAAG.COM:1522/EDWPROD|||SELECT *&#xA;&#xA; &#xA;&#xA;FROM&#xA;&#xA; &#xA;&#xA;APP_RMINV.ART_GC_RULES GC&#xA;&#xA; &#xA;&#xA;WHERE GC.SNAPSHOT_DATE BETWEEN TRUNC(SYSDATE)-7 AND TRUNC(SYSDATE)" type="String" />
#         <Field name="RULE ID" size="512" source="File: oci:RMOR_PROD/__EncPwd1__@LOADING.DATAWAREHOUSE.DB.INSIDEAAG.COM:1522/EDWPROD|||SELECT *&#xA;&#xA; &#xA;&#xA;FROM&#xA;&#xA; &#xA;&#xA;APP_RMINV.ART_GC_RULES GC&#xA;&#xA; &#xA;&#xA;WHERE GC.SNAPSHOT_DATE BETWEEN TRUNC(SYSDATE)-7 AND TRUNC(SYSDATE)" type="V_String" />
#         <Field name="VICEVERSA" size="512" source="File: oci:RMOR_PROD/__EncPwd1__@LOADING.DATAWAREHOUSE.DB.INSIDEAAG.COM:1522/EDWPROD|||SELECT *&#xA;&#xA; &#xA;&#xA;FROM&#xA;&#xA; &#xA;&#xA;APP_RMINV.ART_GC_RULES GC&#xA;&#xA; &#xA;&#xA;WHERE GC.SNAPSHOT_DATE BETWEEN TRUNC(SYSDATE)-7 AND TRUNC(SYSDATE)" type="V_String" />
#         <Field name="TAGS" size="512" source="File: oci:RMOR_PROD/__EncPwd1__@LOADING.DATAWAREHOUSE.DB.INSIDEAAG.COM:1522/EDWPROD|||SELECT *&#xA;&#xA; &#xA;&#xA;FROM&#xA;&#xA; &#xA;&#xA;APP_RMINV.ART_GC_RULES GC&#xA;&#xA; &#xA;&#xA;WHERE GC.SNAPSHOT_DATE BETWEEN TRUNC(SYSDATE)-7 AND TRUNC(SYSDATE)" type="V_String" />
#         <Field name="ORIG" size="512" source="File: oci:RMOR_PROD/__EncPwd1__@LOADING.DATAWAREHOUSE.DB.INSIDEAAG.COM:1522/EDWPROD|||SELECT *&#xA;&#xA; &#xA;&#xA;FROM&#xA;&#xA; &#xA;&#xA;APP_RMINV.ART_GC_RULES GC&#xA;&#xA; &#xA;&#xA;WHERE GC.SNAPSHOT_DATE BETWEEN TRUNC(SYSDATE)-7 AND TRUNC(SYSDATE)" type="V_String" />
#         <Field name="DEST" size="512" source="File: oci:RMOR_PROD/__EncPwd1__@LOADING.DATAWAREHOUSE.DB.INSIDEAAG.COM:1522/EDWPROD|||SELECT *&#xA;&#xA; &#xA;&#xA;FROM&#xA;&#xA; &#xA;&#xA;APP_RMINV.ART_GC_RULES GC&#xA;&#xA; &#xA;&#xA;WHERE GC.SNAPSHOT_DATE BETWEEN TRUNC(SYSDATE)-7 AND TRUNC(SYSDATE)" type="V_String" />
#         <Field name="DOW" size="512" source="File: oci:RMOR_PROD/__EncPwd1__@LOADING.DATAWAREHOUSE.DB.INSIDEAAG.COM:1522/EDWPROD|||SELECT *&#xA;&#xA; &#xA;&#xA;FROM&#xA;&#xA; &#xA;&#xA;APP_RMINV.ART_GC_RULES GC&#xA;&#xA; &#xA;&#xA;WHERE GC.SNAPSHOT_DATE BETWEEN TRUNC(SYSDATE)-7 AND TRUNC(SYSDATE)" type="V_String" />
#         <Field name="START_DATE" source="File: oci:RMOR_PROD/__EncPwd1__@LOADING.DATAWAREHOUSE.DB.INSIDEAAG.COM:1522/EDWPROD|||SELECT *&#xA;&#xA; &#xA;&#xA;FROM&#xA;&#xA; &#xA;&#xA;APP_RMINV.ART_GC_RULES GC&#xA;&#xA; &#xA;&#xA;WHERE GC.SNAPSHOT_DATE BETWEEN TRUNC(SYSDATE)-7 AND TRUNC(SYSDATE)" type="DateTime" />
#         <Field name="END_DATE" source="File: oci:RMOR_PROD/__EncPwd1__@LOADING.DATAWAREHOUSE.DB.INSIDEAAG.COM:1522/EDWPROD|||SELECT *&#xA;&#xA; &#xA;&#xA;FROM&#xA;&#xA; &#xA;&#xA;APP_RMINV.ART_GC_RULES GC&#xA;&#xA; &#xA;&#xA;WHERE GC.SNAPSHOT_DATE BETWEEN TRUNC(SYSDATE)-7 AND TRUNC(SYSDATE)" type="DateTime" />
#         <Field name="SELL_START_DATE" source="File: oci:RMOR_PROD/__EncPwd1__@LOADING.DATAWAREHOUSE.DB.INSIDEAAG.COM:1522/EDWPROD|||SELECT *&#xA;&#xA; &#xA;&#xA;FROM&#xA;&#xA; &#xA;&#xA;APP_RMINV.ART_GC_RULES GC&#xA;&#xA; &#xA;&#xA;WHERE GC.SNAPSHOT_DATE BETWEEN TRUNC(SYSDATE)-7 AND TRUNC(SYSDATE)" type="DateTime" />
#         <Field name="SELL_END_DATE" source="File: oci:RMOR_PROD/__EncPwd1__@LOADING.DATAWAREHOUSE.DB.INSIDEAAG.COM:1522/EDWPROD|||SELECT *&#xA;&#xA; &#xA;&#xA;FROM&#xA;&#xA; &#xA;&#xA;APP_RMINV.ART_GC_RULES GC&#xA;&#xA; &#xA;&#xA;WHERE GC.SNAPSHOT_DATE BETWEEN TRUNC(SYSDATE)-7 AND TRUNC(SYSDATE)" type="DateTime" />
#         <Field name="SEASON" size="100" source="File: oci:RMOR_PROD/__EncPwd1__@LOADING.DATAWAREHOUSE.DB.INSIDEAAG.COM:1522/EDWPROD|||SELECT *&#xA;&#xA; &#xA;&#xA;FROM&#xA;&#xA; &#xA;&#xA;APP_RMINV.ART_GC_RULES GC&#xA;&#xA; &#xA;&#xA;WHERE GC.SNAPSHOT_DATE BETWEEN TRUNC(SYSDATE)-7 AND TRUNC(SYSDATE)" type="V_String" />
#         <Field name="HOLIDAY_NAME" size="100" source="File: oci:RMOR_PROD/__EncPwd1__@LOADING.DATAWAREHOUSE.DB.INSIDEAAG.COM:1522/EDWPROD|||SELECT *&#xA;&#xA; &#xA;&#xA;FROM&#xA;&#xA; &#xA;&#xA;APP_RMINV.ART_GC_RULES GC&#xA;&#xA; &#xA;&#xA;WHERE GC.SNAPSHOT_DATE BETWEEN TRUNC(SYSDATE)-7 AND TRUNC(SYSDATE)" type="V_String" />
#         <Field name="HOLIDAY_FLAG" source="File: oci:RMOR_PROD/__EncPwd1__@LOADING.DATAWAREHOUSE.DB.INSIDEAAG.COM:1522/EDWPROD|||SELECT *&#xA;&#xA; &#xA;&#xA;FROM&#xA;&#xA; &#xA;&#xA;APP_RMINV.ART_GC_RULES GC&#xA;&#xA; &#xA;&#xA;WHERE GC.SNAPSHOT_DATE BETWEEN TRUNC(SYSDATE)-7 AND TRUNC(SYSDATE)" type="Double" />
#         <Field name="START_TIME" size="512" source="File: oci:RMOR_PROD/__EncPwd1__@LOADING.DATAWAREHOUSE.DB.INSIDEAAG.COM:1522/EDWPROD|||SELECT *&#xA;&#xA; &#xA;&#xA;FROM&#xA;&#xA; &#xA;&#xA;APP_RMINV.ART_GC_RULES GC&#xA;&#xA; &#xA;&#xA;WHERE GC.SNAPSHOT_DATE BETWEEN TRUNC(SYSDATE)-7 AND TRUNC(SYSDATE)" type="V_String" />
#         <Field name="END_TIME" size="512" source="File: oci:RMOR_PROD/__EncPwd1__@LOADING.DATAWAREHOUSE.DB.INSIDEAAG.COM:1522/EDWPROD|||SELECT *&#xA;&#xA; &#xA;&#xA;FROM&#xA;&#xA; &#xA;&#xA;APP_RMINV.ART_GC_RULES GC&#xA;&#xA; &#xA;&#xA;WHERE GC.SNAPSHOT_DATE BETWEEN TRUNC(SYSDATE)-7 AND TRUNC(SYSDATE)" type="V_String" />
#         <Field name="FFLabel" size="512" source="File: oci:RMOR_PROD/__EncPwd1__@LOADING.DATAWAREHOUSE.DB.INSIDEAAG.COM:1522/EDWPROD|||SELECT *&#xA;&#xA; &#xA;&#xA;FROM&#xA;&#xA; &#xA;&#xA;APP_RMINV.ART_GC_RULES GC&#xA;&#xA; &#xA;&#xA;WHERE GC.SNAPSHOT_DATE BETWEEN TRUNC(SYSDATE)-7 AND TRUNC(SYSDATE)" type="V_String" />
#         <Field name="FromDtd" size="512" source="File: oci:RMOR_PROD/__EncPwd1__@LOADING.DATAWAREHOUSE.DB.INSIDEAAG.COM:1522/EDWPROD|||SELECT *&#xA;&#xA; &#xA;&#xA;FROM&#xA;&#xA; &#xA;&#xA;APP_RMINV.ART_GC_RULES GC&#xA;&#xA; &#xA;&#xA;WHERE GC.SNAPSHOT_DATE BETWEEN TRUNC(SYSDATE)-7 AND TRUNC(SYSDATE)" type="V_String" />
#         <Field name="KeepDmd" size="512" source="File: oci:RMOR_PROD/__EncPwd1__@LOADING.DATAWAREHOUSE.DB.INSIDEAAG.COM:1522/EDWPROD|||SELECT *&#xA;&#xA; &#xA;&#xA;FROM&#xA;&#xA; &#xA;&#xA;APP_RMINV.ART_GC_RULES GC&#xA;&#xA; &#xA;&#xA;WHERE GC.SNAPSHOT_DATE BETWEEN TRUNC(SYSDATE)-7 AND TRUNC(SYSDATE)" type="V_String" />
#         <Field name="PreOthFF" size="512" source="File: oci:RMOR_PROD/__EncPwd1__@LOADING.DATAWAREHOUSE.DB.INSIDEAAG.COM:1522/EDWPROD|||SELECT *&#xA;&#xA; &#xA;&#xA;FROM&#xA;&#xA; &#xA;&#xA;APP_RMINV.ART_GC_RULES GC&#xA;&#xA; &#xA;&#xA;WHERE GC.SNAPSHOT_DATE BETWEEN TRUNC(SYSDATE)-7 AND TRUNC(SYSDATE)" type="V_String" />
#         <Field name="MAX_1" size="6" source="File: oci:RMOR_PROD/__EncPwd1__@LOADING.DATAWAREHOUSE.DB.INSIDEAAG.COM:1522/EDWPROD|||SELECT *&#xA;&#xA; &#xA;&#xA;FROM&#xA;&#xA; &#xA;&#xA;APP_RMINV.ART_GC_RULES GC&#xA;&#xA; &#xA;&#xA;WHERE GC.SNAPSHOT_DATE BETWEEN TRUNC(SYSDATE)-7 AND TRUNC(SYSDATE)" type="String" />
#         <Field name="MAX_2" size="6" source="File: oci:RMOR_PROD/__EncPwd1__@LOADING.DATAWAREHOUSE.DB.INSIDEAAG.COM:1522/EDWPROD|||SELECT *&#xA;&#xA; &#xA;&#xA;FROM&#xA;&#xA; &#xA;&#xA;APP_RMINV.ART_GC_RULES GC&#xA;&#xA; &#xA;&#xA;WHERE GC.SNAPSHOT_DATE BETWEEN TRUNC(SYSDATE)-7 AND TRUNC(SYSDATE)" type="String" />
#         <Field name="MAX_3" size="6" source="File: oci:RMOR_PROD/__EncPwd1__@LOADING.DATAWAREHOUSE.DB.INSIDEAAG.COM:1522/EDWPROD|||SELECT *&#xA;&#xA; &#xA;&#xA;FROM&#xA;&#xA; &#xA;&#xA;APP_RMINV.ART_GC_RULES GC&#xA;&#xA; &#xA;&#xA;WHERE GC.SNAPSHOT_DATE BETWEEN TRUNC(SYSDATE)-7 AND TRUNC(SYSDATE)" type="String" />
#         <Field name="MAX_4" size="6" source="File: oci:RMOR_PROD/__EncPwd1__@LOADING.DATAWAREHOUSE.DB.INSIDEAAG.COM:1522/EDWPROD|||SELECT *&#xA;&#xA; &#xA;&#xA;FROM&#xA;&#xA; &#xA;&#xA;APP_RMINV.ART_GC_RULES GC&#xA;&#xA; &#xA;&#xA;WHERE GC.SNAPSHOT_DATE BETWEEN TRUNC(SYSDATE)-7 AND TRUNC(SYSDATE)" type="String" />
#         <Field name="MAX_5" size="6" source="File: oci:RMOR_PROD/__EncPwd1__@LOADING.DATAWAREHOUSE.DB.INSIDEAAG.COM:1522/EDWPROD|||SELECT *&#xA;&#xA; &#xA;&#xA;FROM&#xA;&#xA; &#xA;&#xA;APP_RMINV.ART_GC_RULES GC&#xA;&#xA; &#xA;&#xA;WHERE GC.SNAPSHOT_DATE BETWEEN TRUNC(SYSDATE)-7 AND TRUNC(SYSDATE)" type="String" />
#         <Field name="MAX_6" size="6" source="File: oci:RMOR_PROD/__EncPwd1__@LOADING.DATAWAREHOUSE.DB.INSIDEAAG.COM:1522/EDWPROD|||SELECT *&#xA;&#xA; &#xA;&#xA;FROM&#xA;&#xA; &#xA;&#xA;APP_RMINV.ART_GC_RULES GC&#xA;&#xA; &#xA;&#xA;WHERE GC.SNAPSHOT_DATE BETWEEN TRUNC(SYSDATE)-7 AND TRUNC(SYSDATE)" type="String" />
#         <Field name="MAX_7" size="6" source="File: oci:RMOR_PROD/__EncPwd1__@LOADING.DATAWAREHOUSE.DB.INSIDEAAG.COM:1522/EDWPROD|||SELECT *&#xA;&#xA; &#xA;&#xA;FROM&#xA;&#xA; &#xA;&#xA;APP_RMINV.ART_GC_RULES GC&#xA;&#xA; &#xA;&#xA;WHERE GC.SNAPSHOT_DATE BETWEEN TRUNC(SYSDATE)-7 AND TRUNC(SYSDATE)" type="String" />
#         <Field name="MIN_1" size="6" source="File: oci:RMOR_PROD/__EncPwd1__@LOADING.DATAWAREHOUSE.DB.INSIDEAAG.COM:1522/EDWPROD|||SELECT *&#xA;&#xA; &#xA;&#xA;FROM&#xA;&#xA; &#xA;&#xA;APP_RMINV.ART_GC_RULES GC&#xA;&#xA; &#xA;&#xA;WHERE GC.SNAPSHOT_DATE BETWEEN TRUNC(SYSDATE)-7 AND TRUNC(SYSDATE)" type="String" />
#         <Field name="MIN_2" size="6" source="File: oci:RMOR_PROD/__EncPwd1__@LOADING.DATAWAREHOUSE.DB.INSIDEAAG.COM:1522/EDWPROD|||SELECT *&#xA;&#xA; &#xA;&#xA;FROM&#xA;&#xA; &#xA;&#xA;APP_RMINV.ART_GC_RULES GC&#xA;&#xA; &#xA;&#xA;WHERE GC.SNAPSHOT_DATE BETWEEN TRUNC(SYSDATE)-7 AND TRUNC(SYSDATE)" type="String" />
#         <Field name="MIN_3" size="6" source="File: oci:RMOR_PROD/__EncPwd1__@LOADING.DATAWAREHOUSE.DB.INSIDEAAG.COM:1522/EDWPROD|||SELECT *&#xA;&#xA; &#xA;&#xA;FROM&#xA;&#xA; &#xA;&#xA;APP_RMINV.ART_GC_RULES GC&#xA;&#xA; &#xA;&#xA;WHERE GC.SNAPSHOT_DATE BETWEEN TRUNC(SYSDATE)-7 AND TRUNC(SYSDATE)" type="String" />
#         <Field name="MIN_4" size="6" source="File: oci:RMOR_PROD/__EncPwd1__@LOADING.DATAWAREHOUSE.DB.INSIDEAAG.COM:1522/EDWPROD|||SELECT *&#xA;&#xA; &#xA;&#xA;FROM&#xA;&#xA; &#xA;&#xA;APP_RMINV.ART_GC_RULES GC&#xA;&#xA; &#xA;&#xA;WHERE GC.SNAPSHOT_DATE BETWEEN TRUNC(SYSDATE)-7 AND TRUNC(SYSDATE)" type="String" />
#         <Field name="MIN_5" size="6" source="File: oci:RMOR_PROD/__EncPwd1__@LOADING.DATAWAREHOUSE.DB.INSIDEAAG.COM:1522/EDWPROD|||SELECT *&#xA;&#xA; &#xA;&#xA;FROM&#xA;&#xA; &#xA;&#xA;APP_RMINV.ART_GC_RULES GC&#xA;&#xA; &#xA;&#xA;WHERE GC.SNAPSHOT_DATE BETWEEN TRUNC(SYSDATE)-7 AND TRUNC(SYSDATE)" type="String" />
#         <Field name="MIN_6" size="6" source="File: oci:RMOR_PROD/__EncPwd1__@LOADING.DATAWAREHOUSE.DB.INSIDEAAG.COM:1522/EDWPROD|||SELECT *&#xA;&#xA; &#xA;&#xA;FROM&#xA;&#xA; &#xA;&#xA;APP_RMINV.ART_GC_RULES GC&#xA;&#xA; &#xA;&#xA;WHERE GC.SNAPSHOT_DATE BETWEEN TRUNC(SYSDATE)-7 AND TRUNC(SYSDATE)" type="String" />
#         <Field name="MIN_7" size="6" source="File: oci:RMOR_PROD/__EncPwd1__@LOADING.DATAWAREHOUSE.DB.INSIDEAAG.COM:1522/EDWPROD|||SELECT *&#xA;&#xA; &#xA;&#xA;FROM&#xA;&#xA; &#xA;&#xA;APP_RMINV.ART_GC_RULES GC&#xA;&#xA; &#xA;&#xA;WHERE GC.SNAPSHOT_DATE BETWEEN TRUNC(SYSDATE)-7 AND TRUNC(SYSDATE)" type="String" />
#         <Field name="SCALE_1" size="6" source="File: oci:RMOR_PROD/__EncPwd1__@LOADING.DATAWAREHOUSE.DB.INSIDEAAG.COM:1522/EDWPROD|||SELECT *&#xA;&#xA; &#xA;&#xA;FROM&#xA;&#xA; &#xA;&#xA;APP_RMINV.ART_GC_RULES GC&#xA;&#xA; &#xA;&#xA;WHERE GC.SNAPSHOT_DATE BETWEEN TRUNC(SYSDATE)-7 AND TRUNC(SYSDATE)" type="String" />
#         <Field name="SCALE_2" size="6" source="File: oci:RMOR_PROD/__EncPwd1__@LOADING.DATAWAREHOUSE.DB.INSIDEAAG.COM:1522/EDWPROD|||SELECT *&#xA;&#xA; &#xA;&#xA;FROM&#xA;&#xA; &#xA;&#xA;APP_RMINV.ART_GC_RULES GC&#xA;&#xA; &#xA;&#xA;WHERE GC.SNAPSHOT_DATE BETWEEN TRUNC(SYSDATE)-7 AND TRUNC(SYSDATE)" type="String" />
#         <Field name="SCALE_3" size="6" source="File: oci:RMOR_PROD/__EncPwd1__@LOADING.DATAWAREHOUSE.DB.INSIDEAAG.COM:1522/EDWPROD|||SELECT *&#xA;&#xA; &#xA;&#xA;FROM&#xA;&#xA; &#xA;&#xA;APP_RMINV.ART_GC_RULES GC&#xA;&#xA; &#xA;&#xA;WHERE GC.SNAPSHOT_DATE BETWEEN TRUNC(SYSDATE)-7 AND TRUNC(SYSDATE)" type="String" />
#         <Field name="SCALE_4" size="6" source="File: oci:RMOR_PROD/__EncPwd1__@LOADING.DATAWAREHOUSE.DB.INSIDEAAG.COM:1522/EDWPROD|||SELECT *&#xA;&#xA; &#xA;&#xA;FROM&#xA;&#xA; &#xA;&#xA;APP_RMINV.ART_GC_RULES GC&#xA;&#xA; &#xA;&#xA;WHERE GC.SNAPSHOT_DATE BETWEEN TRUNC(SYSDATE)-7 AND TRUNC(SYSDATE)" type="String" />
#         <Field name="SCALE_5" size="6" source="File: oci:RMOR_PROD/__EncPwd1__@LOADING.DATAWAREHOUSE.DB.INSIDEAAG.COM:1522/EDWPROD|||SELECT *&#xA;&#xA; &#xA;&#xA;FROM&#xA;&#xA; &#xA;&#xA;APP_RMINV.ART_GC_RULES GC&#xA;&#xA; &#xA;&#xA;WHERE GC.SNAPSHOT_DATE BETWEEN TRUNC(SYSDATE)-7 AND TRUNC(SYSDATE)" type="String" />
#         <Field name="SCALE_6" size="6" source="File: oci:RMOR_PROD/__EncPwd1__@LOADING.DATAWAREHOUSE.DB.INSIDEAAG.COM:1522/EDWPROD|||SELECT *&#xA;&#xA; &#xA;&#xA;FROM&#xA;&#xA; &#xA;&#xA;APP_RMINV.ART_GC_RULES GC&#xA;&#xA; &#xA;&#xA;WHERE GC.SNAPSHOT_DATE BETWEEN TRUNC(SYSDATE)-7 AND TRUNC(SYSDATE)" type="String" />
#         <Field name="SCALE_7" size="6" source="File: oci:RMOR_PROD/__EncPwd1__@LOADING.DATAWAREHOUSE.DB.INSIDEAAG.COM:1522/EDWPROD|||SELECT *&#xA;&#xA; &#xA;&#xA;FROM&#xA;&#xA; &#xA;&#xA;APP_RMINV.ART_GC_RULES GC&#xA;&#xA; &#xA;&#xA;WHERE GC.SNAPSHOT_DATE BETWEEN TRUNC(SYSDATE)-7 AND TRUNC(SYSDATE)" type="String" />
#       </RecordInfo>
#     </MetaInfo>
#   </Properties>
#   <EngineSettings EngineDll="AlteryxBasePluginsEngine.dll" EngineDllEntryPoint="AlteryxDbFileInput" />
# </Node>