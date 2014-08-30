#======================================================================================
#             Startup of ModelioScribes Framework
#--------------------------------------------------------------------------------------
# Modelio provides a lot of features for the development of plugin in java but no
# facilities is given for developing in python beyond simple monolithic macro development.
# This very small framework supports to following features
# - support for code development/execution outside modelio workspace macro directory
# - modular development of python modules with reloading features in development mode
# - inclusion of regular python and java libraries thanks to python/java path management
# - support for directory management allowing to develop code independently from execution
# The framework provides 3 classes:
# - ScribesEnv
# - Scribe
# - ScribeExecution 
# Only ScribeExecution is used directly when a macro is launched. 
#======================================================================================


import os
import sys
import java.lang
import java.net 
import encodings   # needed to avoid failures when loading some modules

class ScribesEnv(object):
  def __init__(self):
    self.home = self._computeHome()
    self.initial_class_loader = sys.getClassLoader()
    self._addAllModulesAndPythonLibraryDirectoriesToPath()
  #-------------------------------------------------------------------------------------- 
  #  Path management.
  #--------------------------------------------------------------------------------------  

  def getWorkspaceMacrosDirectory(self):
    """ Return the path to the macros directory within the workspace
    """
    workspace = Modelio.getInstance().getContext().getWorkspacePath().toString()
    return os.path.join(workspace,'macros')
    
  def _ScribeHomeHelp(self):
    print "The environment variable SCRIBES_HOME is currently not set."
    print "Its value must be set to the path of the directory  ModelioScribes."
    print "The expected value might look like C:\\DEV\\ModelioScribes."
    print "Please set this variable using your operating system and"
    print "restart modelio after doing so."
    print
    print "On Windows environment variables can be changed via the interface"
    print "using something like the following:"
    print "'Settings' > 'System properties' > 'Advanced' > 'Environment variables'."
    print "On UNIX systems, this could be done in your .bashrc file for instance."
    print "Check your operating system documentation to see how to set an"
    print "an environment variable."
    
  def _computeHome(self):
    """ Find the location of ModelioScribes directory. 
        (1) check first the environment variable SCRIBES_HOME,
        (2) otherwise search in the "macros" directory of the workspace,
        (3) otherwise search in the ".modelio" directory of the user home.
        Display messages in case of errors and raise an exception.
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
      # (2) Look in the macros directory of the workspace
      home = os.path.join(_getWorkspaceMacrosDirectory(),'ModelioScribes')
      if os.path.isdir(home):
        return home
      else:
        # (3) Look in the ".modelio" directory of the user home. 
        home = os.path.join(os.path.expanduser("~"),'.modelio','ModelioScribes')
        if os.path.isdir(home):
          return home
        else:
          # error
          self._ScribeHomeHelp()
          raise Exception("SCRIBES_HOME is not defined")
  
  def getHome(self):
    return self.home
    
  def getDirectory(self,pathElements=[]):
    """ Return a path to a file or a dir starting with modelioscribe home
        For instance getPath(['commons','tests']) returns a directory name but
        getPath(['commons','tests','README.md']) returns a filename.
        If nothing is provided then return the home of modelio scribes.
        getPath()
    """
    path = self.getHome()
    for e in pathElements:
      path = os.path.join(path,e)
    return path
    

  def _addDirectoryToPath(self,directory):
    """ Add the directory to the system path if it does not exist already.
        Check that the directory is valid. Otherwise a message is simply issued.
        Returns a boolean indicating if this was a success or not but no
        exception is raised.
    """
    if not directory in sys.path:
      if os.path.isdir(directory):
        sys.path.extend([directory])
      else:
        print "WARNING: "+directory+" cannot be added to the path. It is not a valid directory"
    
    
    

  #-------------------------------------------------------------------------------------- 
  #  Module Management.
  #--------------------------------------------------------------------------------------  

  def _addAllModulesAndPythonLibraryDirectoriesToPath(self):
    """ Add the directory following these patterns to the path
        <HOME>/scribes/<DIRECTORY>/modules
        <HOME>/scribes/<DIRECTORY>/libs/python
        <HOME>/commons/modules
        <HOME>/libs/python
        Modules take precedence over local libs
    """
    dirs = []
    for name in os.listdir(self.home+os.sep+'scribes'):
      for location in [name+os.sep+'modules',name+os.sep+'libs'+os.sep+'python']:
        dirs.append(os.path.join(self.home,'scribes',location))
    dirs.append(os.path.join(self.home,'commons','modules'))
    dirs.append(os.path.join(self.home,'libs','python'))
    for dir in dirs:
      if os.path.isdir(dir):
          self._addDirectoryToPath(dir)

  def loadModule(self,modulenames,reload=False):
    """ Load/reload a (list of) module(s). Reload if the second parameter is true.
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
    

  #-------------------------------------------------------------------------------------
  #  Python Libraries
  #-------------------------------------------------------------------------------------


  #-------------------------------------------------------------------------------------- 
  #  Java Librairies
  #--------------------------------------------------------------------------------------   

  def setJavaPath(self,pathEntries,baseDirectory=None):
    urls = []
    for pe in pathEntries:
      urls.append(java.net.URL("file:"+pe))
    sys.setClassLoader(java.net.URLClassLoader(urls))
  def restoreJavaPath(self):
    sys.setClassLoader(self.initial_class_loader)
  # def __str__(self):
  #    sep = java.lang.System.getProperty("path.separator")
  #    urls = sys.getClassLoader().getURLs()
  #    return sep.join([url.getPath() for url in urls])    
        

        
        
class Scribe(object):
  def __init__(self,scribename):
    global SCRIBES_ENV #RO
    self.env = SCRIBES_ENV
    self.scribeName = scribename
    #-- setup directories attribute
    self.directories = self._computeDirectoryMap()
    
        
  def _computeDirectoryMap(self):
    globalMap = {
      'home'                : '', 
      'commons'             : 'commons',
      'commons.modules'     : 'commons modules',
      'commons.docs'        : 'commons docs',
      'commons.tests'       : 'commons tests',
      'commons.res'         : 'commons res',
      'libs.java'           : 'libs java',
      'libs.python'         : 'libs python',
      }
    scribeMap = {
      'scribe'              : '',
      'scribe.res'          : 'res',
      'scribe.tests'        : 'tests',
      'scribe.docs'         : 'docs',
      'scribe.modules'      : 'modules',
      'scribe.libs.java'    : 'libs java',
      'scribe.libs.python'  : 'libs python',
      }
    map = {}
    for e in globalMap:
      map[e] = self.env.getDirectory(globalMap[e].split(' '))
    for e in scribeMap:
      map[e] = self.env.getDirectory(['scribes',self.scribeName]+scribeMap[e].split(' '))
    return map              
        
        
        
        
class ScribeExecution(Scribe):
  def __init__(self,scribename,entryFunName,modules=[],debug=None):
    """ Execute a particular scribe entry point.
    """
    
    global SCRIBE
    Scribe.__init__(self,scribename)
    self.env.scribe = self   # set the current scribe just for information
    SCRIBE = self
    
    #--- collect selectedElements, modelingSession, session from modelio variables
    global selectedElements #RO
    self.selectedElements = selectedElements 
    global modelingSession #RO
    self.modelingSession = modelingSession
    global selection #RO
    self.selection = selection
    
    #--- compute debug flag, based on the parameter or DEBUG global variable otherwise
    if debug is None:
      try: 
        global DEBUG
        self.debug = DEBUG
      except:
        self.debug = DEBUG
    else:
      self.debug = debug
    
    #--- compute 
    (m,f) = self._computeEntry(scribename,entryFunName)
    self.entryModule = m
    self.entryFunName = f
    
    #-- load the list of modules specified (plus the entry modules)
    self.modules = modules
    if self.entryModule not in modules:
      self.modules += [self.entryModule]         
    self.env.loadModule(self.modules,self.debug)
    
    #-- execute the entry function
    self.runEntryFunction()
    
      
  def runEntryFunction(self):
    self.env.scribe = self   # set the current scribe
    exec( "import "+self.entryModule+";" \
          +self.entryFunName+"(self)" )
          
    
  def _computeEntry(self,scribename,entryFunName):
    """ compute the name of the entryModule from the entry function name provided
    """
    lastDotIndex = entryFunName.rfind('.')
    if lastDotIndex == -1:
      # if the entry function is not qualified, then deduce the module from scribename
      entryModule = scribename.lower()
      entryFunName = entryModule+"."+entryFunName
    else:
      # take the qualifier
      entryModule = entryFunName[0:lastDotIndex]
      entryFunName = entryFunName
    return (entryModule,entryFunName)


    

    


#-------------------------------------------------------------------------------------- 
#  Global Framework Startup.
#--------------------------------------------------------------------------------------   

try:
  SCRIBES_ENV
except:  
  SCRIBES_ENV = ScribesEnv()

  






