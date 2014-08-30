DEBUG=True
#===== start the modelioscribes framework ==========================================
import os 
WORKSPACE_DIRECTORY=Modelio.getInstance().getContext().getWorkspacePath().toString()
execfile(os.path.join(WORKSPACE_DIRECTORY,'macros','modelioscribes_startup.py'))
#===================================================================================


ScribeExecution('SandScribe',"poitest.macro_poitest")
#ScribeExecution('SandScribe',"pydtest.macro_pydtest")
ScribeExecution('SandScribe',"oossmapper.macro_oossmapper",["ooss"])
ScribeExecution('SandScribe',"googlesheet.macro_googlesheet")
ScribeExecution('SandScribe',"treetester.macro_treetester",["textual_tree"])
ScribeExecution('SandScribe',"sandbox.macro_sandbox")
ScribeExecution('SandScribe',"helloworld.macro_helloworld")
