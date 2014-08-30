def macro_helloworld(scribe):
  print "hello world!"
  print
  print "The following elements are selected:"
  for e in scribe.selectedElements:
    print e
  print "The following directories are defined:"
  print
  for d in scribe.directories:
    print d," is ",scribe.directories[d]
