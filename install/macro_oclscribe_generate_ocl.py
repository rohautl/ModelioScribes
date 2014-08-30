DEBUG=True
#===== start the modelioscribes framework ==========================================
import os
WORKSPACE_DIRECTORY=Modelio.getInstance().getContext().getWorkspacePath().toString()
execfile(os.path.join(WORKSPACE_DIRECTORY,'macros','modelioscribes_startup.py'))
#===================================================================================

ScribeExecution('OCLScribe',"oclscribe.macro_generate_ocl",["oclscribe_generator"])
    



