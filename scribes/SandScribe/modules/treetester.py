def macro_treetester(scribe):
  from textual_tree import TextualTreeReader
  import os
  testdir=os.path.join(scribe.directories['commons'],'tests','testCases')
  testfile=os.path.join(testdir,'textualTree-nested-updown-ok.txt')
  t = TextualTreeReader(testfile).getTextualTree()
  print t.text()
