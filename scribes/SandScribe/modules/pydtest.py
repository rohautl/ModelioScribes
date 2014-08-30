#---------------------------------------------------------------------------------------
# pydrivetest
#---------------------------------------------------------------------------------------
#For PyDrive to work with oauth
#  webbrowser -> 
#    download http://bugs.jython.org/file1402 on put webbrowser.py in the path
#    for explaination: http://bugs.jython.org/issue1762054
#  Patch for httplib2 to avoid ssl problems 
#    PyLib\httplib2:__init__.py:1143:  ca_certs=None, disable_ssl_certificate_validation=True):  #JFE
import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def macro_pydtest(scribe):
  pydtest(scribe)

GAUTH=None
def pydtest(scribe):
  print "READS THE SOURCE IN CASE OF PROBLEMS. PATCHES SHOULD BE APPLIED"

  global GAUTH
  GAUTH = GoogleAuth()
  print GAUTH
  secretFile=scribe.directories['scribe.res']+os.sep+'client_secrets.json'
  print secretFile
  GAUTH.LoadClientConfigFile(secretFile)
  # gauth.LocalWebserverAuth()
  auth_url = GAUTH.GetAuthUrl()
  print "copy this url in a web browser, connect to google if requested, and accept the application"
  print auth_url
  print 'when done copy the code from the resulting url and type in the console'
  print 'import pydtest ; pydtest.cont("...the code...")'

def cont(code):
  GAUTH.Auth(code)
  d = GoogleDrive(GAUTH)
  file1 = d.CreateFile({'title': 'Hello.txt'})  # Create GoogleDriveFile instance with title 'Hello.txt'
  file1.SetContentString('Hello World!') # Set content of the file from given string
  file1.Upload()
  print "Hello.txt has been uploaded"
  return d