#
# CoExplorer
#
# Model/Metamodel co-explorer for Modelio.
#
# Author: jmfavre
#
# Compatibility: Modelio 3.x
#

# Installation:
#   This script should be installed as a workspace macro using standard modelio procedure
#   to add macros. The options to use are the following options:
#      - "Applicable on" : No Selection. The macro is application on any kind of element
#      - "Show in contextual menu" : YES
#      - "Show in toolbar" : YES
#   This script is based on the content of the "lib" directory which must be copied manually
#   in the same directory as this very file. That is, in the directory where this file
#   CoExplorer.py will be installed by modelio through the standard macro installation procedure.
#   Ultimately we should have the following structure 
#          CoExplorer.py             <--- this very file
#             lib/
#                 introspection.py
#                 misc.py
#                 modelioscriptor.py
#                 ...                <--- possibly other jython modules
#                 res/
#                     assoc-1.gif
#                     assoc-n.gif
#                     ...            <--- other resources.
#


# MODULES_TO_RELOAD = []
MODULES_TO_RELOAD = [ "misc", "modelioscriptor", "introspection"  ]

def startup():
  print "The CoExplorer is starting ..."

  #---- add the "lib" directory to the path
  # The code below compute this path and put it in the variable SCRIPT_LIBRARY_DIRECTORY. 
  # Feel free to change it if necessary. Currently the "lib" directory is search within
  # the directory of this very file, but if you may want to change its location you can
  # uncomment the line defining SCRIPT_LIBRARY_DIRECTORY with an absolute path
  try:
    from org.modelio.api.modelio import Modelio
    orgVersion = True
  except:
    orgVersion = False
  import os
  import sys 
  WORKSPACE_DIRECTORY=Modelio.getInstance().getContext().getWorkspacePath().toString()
  if orgVersion:
    MACROS_DIRECTORY=os.path.join(WORKSPACE_DIRECTORY,'macros')
  else:
    MACROS_DIRECTORY=os.path.join(WORKSPACE_DIRECTORY,'.config','macros')
  SCRIPT_LIBRARY_DIRECTORY=os.path.join(MACROS_DIRECTORY,'lib')
  # Uncomment this line and adjust it if you want to put the "lib" directory somewhere else
  # SCRIPT_LIBRARY_DIRECTORY = "C:\\MODELIO3-WORKSPACE\\macros\\lib"
  sys.path.extend([MACROS_DIRECTORY,SCRIPT_LIBRARY_DIRECTORY])
  print "   Current workspace is "+WORKSPACE_DIRECTORY
  print "   "+MACROS_DIRECTORY+" added to script path"
  print "   "+SCRIPT_LIBRARY_DIRECTORY+" added to script path"

  
def displayInitialMessage():
  print
  print "The CoExplorer has been launched in a new window with selectedElements"
  print "You can at any time use the function explore(...elements...) in this script window"
  print "Using 'exp' instead of 'explore' allows to browse the metamodel and javadoc"
  print
  print "Try for instance the following:"
  print "exp(allInstances(Package))            --> explore all packages"
  print "exp(allDiagrams())                    --> explore all diagrams"
  print "explore(allMClasses())                --> explore the metamodel"


#---- check if this is the first time this macro is loaded or not  
try:
  CO_EXPLORER_EXECUTION += 1
  # this is the not the first time
except:
  # this is the first time
  CO_EXPLORER_EXECUTION = 1
  startup()
    

#----- reload and imports the modules (see the variable at the end of script)
if "misc" in MODULES_TO_RELOAD:
  try: del sys.modules["misc"] ; del misc
  except: pass
from misc import *

if "modelioscriptor" in MODULES_TO_RELOAD:
  try: del sys.modules["modelioscriptor"] ; del modelioscriptor
  except: pass
from modelioscriptor import *

if "introspection" in MODULES_TO_RELOAD:
  try: del sys.modules["introspection"] ; del introspection
  except: pass
from introspection import *



#----- Launch a new co-explorer window
n = len(selectedElements)
print
print "explore(selectedElements)     #",n,"element",("" if n<=1 else "s")
coexplorer = explore(selectedElements)

if CO_EXPLORER_EXECUTION==1:
  displayInitialMessage()


