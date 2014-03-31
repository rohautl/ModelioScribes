DEBUG=True
#===== start the modelioscribes framework ==========================================
import os 
WORKSPACE_DIRECTORY=Modelio.getInstance().getContext().getWorkspacePath().toString()
execfile(os.path.join(WORKSPACE_DIRECTORY,'macros','modelioscribes_startup.py'))
#===================================================================================

MODULES=["misc","metascribe_introspection","metascribe"]
scribeStartup('MetaScribe',"macro_coexplorer",selectedElements,MODULES,DEBUG)

  

    



