# Databricks notebook source

# MAGIC %md
# MAGIC # Alteryx Workflow to Databricks Notebook Conversion
# MAGIC
# MAGIC The following code takes the XML contents of an Alteryx workflow file (.yxmd) and converts it to a Databricks notebook
# MAGIC ### Notes on Execution
# MAGIC * Generally, each node in the workflow gets its own cell in the generated notebook.
# MAGIC * Only a limited number of tools are currently supported. For unsupported tools, a placeholder cell will be generated with the metadata of the tool configuration
# MAGIC ### Instructions
# MAGIC 1. Copy the contents of your Workflow(yxmd) file and paste it in place of the "\<PASTE_YXMD_FILE_CONTENTS_HERE\>" string in the cell below
# MAGIC 2. Execute the notebook
# MAGIC 3. The generated notebook will appear in the root level of your user directory

# COMMAND ----------

# MAGIC %pip install databricks-sdk --upgrade
# MAGIC dbutils.library.restartPython()

# COMMAND ----------

import base64
import time

from databricks.sdk import WorkspaceClient
from databricks.sdk.service import workspace

from alteryx2dbx import AlteryxWorkflow


# COMMAND ----------

yxmd_contents = """
    <PASTE_YXMD_FILE_CONTENTS_HERE>
""".strip()

# COMMAND ----------

workflow_object = AlteryxWorkflow.from_string(yxmd_contents)

workflow_name = workflow_object.name

workflow_notebook = workflow_object.to_string()

# COMMAND ----------

w = WorkspaceClient()

notebook_path = f'/Users/{w.current_user.me().user_name}/{workflow_name}'

w.workspace.import_(content=base64.b64encode((workflow_notebook).encode()).decode(),
                    format=workspace.ImportFormat.SOURCE,
                    language=workspace.Language.PYTHON,
                    overwrite=True,
                    path=notebook_path)