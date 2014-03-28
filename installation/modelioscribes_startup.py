import os
import sys

#--------------------------------------------------------------------------------------  
#  Path management.
#--------------------------------------------------------------------------------------  

def _getWorkspaceMacrosDirectory():
  """ Return the path to the macros directory within the workspace
  """
  workspace = Modelio.getInstance().getContext().getWorkspacePath().toString()
  return os.path.join(workspace,'macros')
  
  
def _getHome():
  """ Find the location of ModelioScribes directory. 
      (1) check first the environment variable SCRIBE_HOME.
      (2) If this variable is not set, then search this directory in the "macros"
      directory of the current workspace. 
      Display messages in case of errors but simply returns None.
  """    
  try: 
    # (1) Check first the variable SCRIBES_HOME
    home = os.environ['SCRIBES_HOME']
    if os.path.isdir(home):
      return home
    else:
      print "SCRIBES_HOME is set to '"+home+"' but this is not a valid directory."
      return None
  except:
    # (2) Look in the macros directory
    home = os.path.join(_getWorkspaceMacrosDirectory(),'ModelioScribes')
    if os.path.isdir(home):
      return home
    else:
      print "The environement variable SCRIBES_HOME is currently not set."
      print "Its value must be set to the path of the directory  ModelioScribes."
      print "The expected value might look like C:\\DEV\\ModelioScribes."
      print "Please set this variable using your operating system and"
      print "restart modelio after doing so."
      print "On Windows environment variables can be changed via the interface"
      print "using something like the following:"
      print "'Settings' > 'System properties' > 'Advanced' > 'Environement variables'."
      print "On UNIX systems, this could be done in your .bashrc file for instance."
      print "Check your operating system documentation to see how to set an"
      print "an environment variable."
      return None

def _addDirectoryToPath(directory):
  """ Add the directory to the system path if it does not exist already.
      Check that the directory is valid. Otherwise a message is simply issued.
      Returns a boolean indicating if this was a success or not but no
      exception is raised.
  """
  if not directory in sys.path:
    if os.path.isdir(directory):
      sys.path.extend([directory])
    else:
      print directory+" cannot be added to the path. It is not a valid directory"
  
def _addModulesDirectoriesToPath(home):
  """ Add "<HOME>/<DIRECTORY>/modules" directories to the path
  """
  for name in os.listdir(home):
    modulepath = os.path.join(home,name,'modules')
    if os.path.isdir(modulepath):
      _addDirectoryToPath(modulepath)

def loadModule(modulenames,reload=False):
  """ Load or reload a (list of) module(s) if the second parameter is true.
      - modulenames is either a string or a list of string.
      - reload the module if the reload parameter is true
  """
  if  isinstance(modulenames, basestring):
    modulenames = [ modulenames ]
  for modulename in modulenames:    
    notLoaded = modulename not in sys.modules
    if reload or notLoaded:
      try: 
        del sys.modules[modulename]
        exec( "del "+modulename )
      except:pass
    exec( "import "+modulename )
  

def scribeStartup(scribename,functionname,selectedElements,reload=False):
  modulename = scribename.lower()
  loadModule(modulename,reload)
  directories = {}
  directories['home'] = HOME
  directories['scribe'] = os.path.join(HOME,scribename)
  directories['res'] = os.path.join(directories['scribe'],'res')
  exec( "import "+modulename+ " ; "+modulename+"."+functionname+"(selectedElements,directories)" )
  
    
HOME = _getHome()
if HOME is not None:
  _addModulesDirectoriesToPath(HOME)
  






