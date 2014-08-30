DEBUG=True
#===== start the modelioscribes framework ==========================================
import os 
WORKSPACE_DIRECTORY=Modelio.getInstance().getContext().getWorkspacePath().toString()
execfile(os.path.join(WORKSPACE_DIRECTORY,'macros','modelioscribes_startup.py'))
#===================================================================================

ScribeExecution('MetaScribe',"macro_coexplorer",["metascribe_introspection","gui","misc"])
  

    



