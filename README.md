# Alteryx Workflow to Databricks Notebook Conversion
The included code package takes the XML contents of an Alteryx workflow file (.yxmd) and converts it to a Databricks notebook

### Instructions
Eventually this code will get packaged and published to PyPi, but in the meantime, here are the steps to start using this code from Databricks:
1. In your Databricks workspace, click on the "New+" button and under the "More" section, select "Git Folder".
2. Copy the URL of this repository and paste it into the "Git Repository URL" field. The other fields should populate automatically.
3. In the newly created folder there is a notebook called "conversion_notebook", open that notebook and paste the XML contents of your Alteryx workflow file in place of the "\<PASTE_YXMD_FILE_CONTENTS_HERE\>" string in the second cell.
4. Execute the notebook on a cluster with Runtime version 13.3 or greater
5. A notebook with the same name as your Alteryx workflow will appear in the root of your user directory

### Notes on Execution
* Generally, each node in the workflow gets its own cell in the generated notebook.
* Only a limited number of tools are initially supported. For unsupported tools, a placeholder cell will be generated with the metadata of the tool configuration


### Currently Supported Tools
* Join
* Filter
* Union
* DBInput