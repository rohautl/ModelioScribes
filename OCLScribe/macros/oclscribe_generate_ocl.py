HOME_DIRECTORY = r"C:\DEV\ModelioScribes\OCLScribe"
# CHANGE THE LINE ABOVE TO SET 



#--------------------------------------------------------------------------------------  
#  Path management.
#--------------------------------------------------------------------------------------  
def addModulesAndLibToPath(home_directory):
  """ Add some directories to the path
      (1) add the "macros/lib" directory contained in the workspace 
      (2) add the home directory of this file (see the variable at the top of this file)
      (3) add the "modules" directory within this home 
  """
  import os
  import sys 
  WORKSPACE_DIRECTORY=Modelio.getInstance().getContext().getWorkspacePath().toString()
  MACROS_DIRECTORY=os.path.join(WORKSPACE_DIRECTORY,'macros')
  SCRIPT_LIBRARY_DIRECTORY=os.path.join(MACROS_DIRECTORY,'lib')
  SCRIPT_MODULES_DIRECTORY=os.path.join(home_directory,'modules')
  
  if not os.path.isdir(home_directory):
    print "The variable home_directory in this macro is set to '"+home_directory+"'"
    print "This directory does not exist. You must change the script file .python"
    raise Exception
    
  if not os.path.isdir(SCRIPT_MODULES_DIRECTORY):
    print "The directory '"+SCRIPT_MODULES_DIRECTORY+"' does not exists"
    raise Exception  
  sys.path.extend([MACROS_DIRECTORY,SCRIPT_LIBRARY_DIRECTORY])
  sys.path.extend([home_directory,SCRIPT_MODULES_DIRECTORY])
  
  if DEBUG:
    print "   Current workspace is "+WORKSPACE_DIRECTORY
    print "   "+MACROS_DIRECTORY+" added to script path"
    print "   "+SCRIPT_LIBRARY_DIRECTORY+" added to script path"
    print "   "+home_directory
    print "   "+SCRIPT_MODULES_DIRECTORY+" added to script path"
#--------------------------------------------------------------------------------------  

    

#---- check if this is the first time this macro is loaded or not  
try:
  OCLSCRIBE_EXECUTIONS += 1
  # this is the not the first time
except:
  # this is the first time
  OCLSCRIBE_EXECUTIONS = 1
  addModulesAndLibToPath(HOME_DIRECTORY)
  
#---- (re)load the interface module
try: del sys.modules["oclscribe_interface"] ; del oclscribe_interface
except: pass
from oclscribe_interface import *
  
#---- call the function corresponding to this macro
do_generate_ocl(selectedElements)
    



