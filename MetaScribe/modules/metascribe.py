#==================================================================================
#   Module Interface
#==================================================================================
__all__ = [
  "do_coexplore"
]



#==================================================================================
#   Module Implementation
#==================================================================================

from metascribe_introspection import explore


#---------------------------------------------------------------------------
#  Macro definition
#---------------------------------------------------------------------------

def macro_coexplorer(selectedElements,directories):
  n = len(selectedElements)
  print "explore(selectedElements)     #",n,"element",("" if n<=1 else "s")
  coexplorer = explore(selectedElements)

  
  
  
  

#def displayInitialMessage():
#  print
#  print "The CoExplorer has been launched in a new window with selectedElements"
#  print "You can at any time use the function explore(...elements...) in this script window"
#  print "Using 'exp' instead of 'explore' allows to browse the metamodel and javadoc"
#  print
#  print "Try for instance the following:"
#  print "exp(allInstances(Package))            --> explore all packages"
#  print "exp(allDiagrams())                    --> explore all diagrams"
#  print "explore(allMClasses())                --> explore the metamodel"


#---- check if this is the first time this macro is loaded or not  
#try:
#  CO_EXPLORER_EXECUTION += 1
#  # this is the not the first time
#except:
#  # this is the first time
#  CO_EXPLORER_EXECUTION = 1
#  startup()
  
  

#----- Launch a new co-explorer window
#if CO_EXPLORER_EXECUTION==1:
#  displayInitialMessage()