DEBUG=True
#===== start the modelioscribes framework ==========================================
import os
WORKSPACE_DIRECTORY=Modelio.getInstance().getContext().getWorkspacePath().toString()
execfile(os.path.join(WORKSPACE_DIRECTORY,'macros','modelioscribes_startup.py'))
#===================================================================================

MODULES=["oclscribe","oclscribe_generator"]
scribeStartup('OCLScribe',"macro_generate_ocl",selectedElements,MODULES,DEBUG)
    



