#===================================================================================
# oclscribe
#
# This module provides the interface for the OCLScribe macros
# Currently there is only one macro:
#  - generate_ocl
# For each macro XXX there is a function do_XXX which is called when the macro is
# applied.
#===================================================================================


#-----------------------------------------------------------------------------------
#   Module Interface
#-----------------------------------------------------------------------------------
__all__ = [
  "do_generate_ocl"
]


#-----------------------------------------------------------------------------------
#   Module Implementation
#-----------------------------------------------------------------------------------
MODULES_TO_RELOAD = [ "oclscribe_generator"  ]      # To be updated if necessary


#---------------------------------------------------------------------------
# Import of modules that can be modified during the development
# If a module is stable, remove it from the variable MODULES_TO_RELOAD
# Changes applied to a module will only be visible if it is declared in this
# list. 
#---------------------------------------------------------------------------  

#----- reload and import the modules if necessary
# This list depends on the modules that are used by this script
if "oclscribe_generator" in MODULES_TO_RELOAD:
  try: del sys.modules["oclscribe_generator"] ; del oclscribe_generator
  except: pass
from oclscribe_generator import *

#if "misc" in MODULES_TO_RELOAD:
#  try: del sys.modules["misc"] ; del misc
#  except: pass
#from misc import *

#if "modelioscriptor" in MODULES_TO_RELOAD:
#  try: del sys.modules["modelioscriptor"] ; del modelioscriptor
#  except: pass
#from modelioscriptor import *

#if "introspection" in MODULES_TO_RELOAD:
#  try: del sys.modules["introspection"] ; del introspection
#  except: pass
#from introspection import *



#---------------------------------------------------------------------------
# GUI : 
# The OCL output is generated in a html window
#---------------------------------------------------------------------------
from org.eclipse.swt import SWT
from org.eclipse.swt import *
from org.eclipse.swt.widgets import Text, Composite
from org.eclipse.swt.layout import FillLayout
from org.eclipse.swt.widgets import Shell,Display,Label,Button,Listener
from org.eclipse.swt.browser import Browser
from org.eclipse.swt.layout import GridData,GridLayout
from org.eclipse.swt.custom import ScrolledComposite
from org.eclipse.swt.graphics import Color, Image
class USEWindow(object):
  def __init__(self, title= None, toDisplay= None):


    parentShell = Display.getDefault().getActiveShell()
    self.window = Shell(parentShell, SWT.CLOSE | SWT.RESIZE)
    self.window.setText(title)
    self.window.setLayout(FillLayout())
    self.window.setSize (self.window.computeSize(1400, 500))
    self.text = Browser(self.window, SWT.NONE)
    self.text.setText( \
              "<html><header><style>" +
              "<!--.tab { margin-left: 40px;} .tab2 { margin-left: 80px; }" + 
              " .tab3 { margin-left: 120px; }.tab4 { margin-left: 160px; }-->" +
              "</style></header><body><div style=\"overflow: auto;\">" + 
              toDisplay + "</div></body></html>")
    self.window.open ()
        
#---------------------------------------------------------------------------
#  Process the selection
#---------------------------------------------------------------------------
from org.modelio.metamodel.uml.statik import *
from org.modelio.metamodel.uml.infrastructure import *
from org.modelio.metamodel.mda import Project

def compileSelectedElements(selectedElements):
  toDisplay = ""
  nAssociations_list = []
  associationList = []
  modelElement  = selectedElements.get(0)
  while not isinstance(modelElement, Project):
    modelElement = modelElement.getCompositionOwner()
  toDisplay += "<b>model </b>" +modelElement.getName() + "<br><br>"
  toDisplay += "<b>--enumerations</b><br>"
  for selectedEnumerations in selectedElements:
    toDisplay += compileEnumerations(selectedEnumerations)
  toDisplay += "<b>--classes</b><br>"
  for selectedClasses in selectedElements:
    toDisplay += compileClasses(selectedClasses)
  toDisplay = toDisplay +  "<b>--associations</b><br>"
  for selectedAssociations in selectedElements:
    toDisplay += compileAssociations(selectedAssociations, nAssociations_list, associationList)  
  toDisplay = toDisplay +  "<b>-- OCL constraints</b><br>"
  for selectedConstraints in selectedElements:
    toDisplay = toDisplay + compileConstraints(selectedConstraints)
  return toDisplay

  
#---------------------------------------------------------------------------
#  Macro definition
#---------------------------------------------------------------------------
def macro_generate_ocl(selectedElements,directories): 
  if (selectedElements.size() > 0):
    toDisplay = compileSelectedElements(selectedElements)
    USEWindow(title = "USE Generation", toDisplay = toDisplay)
  else:
    USEWindow(title = "USE Code Generation", toDisplay = "No Element has been selected") 