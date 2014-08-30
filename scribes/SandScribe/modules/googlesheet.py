import sys
from encodings import iso8859_1

def macro_googlesheet(self):
  # code 
  #print "sys.version ----------- %s" % sys.version
  #print "default encoding ------ %s" % sys.getdefaultencoding()
  # print
  # print "loading gspread modules"
  # try:
  #   del sys.modules["gspread.client"] ; del gspread.client
  #   del sys.modules["gspread.httpsession"] ; del gspread.httpsession
  #   del sys.modules["gspread"] ; del gspread
  # except: pass
  # import gspread.client
  import gspread
  print "gspread modules loaded"

  print "connecting to google ...",
  gc = gspread.login('jeanmariefavre.2.0', 'avectar6566')
  print "done"

  doc = "test"
  print "opening document "+doc+" ... ",
  spsht = gc.open(doc)
  print "done"
  print "updating a cell ...",
  wks = spsht.sheet1
  wks.update_acell("B2","toto") 
  print "done"
  print "sheets are:",
  for w in spsht.worksheets():
    print "  ",w
  print "end"

#===============================================================
# https://developers.google.com/apps-script/reference/spreadsheet/


# SpreadsheetApp	  Open Google Sheets files and to create new ones.
  # create
  # open
  # active
  # ui
# Spreadsheet	      Access and modify Google Sheets files.
  # editor
  # viewer
  # active
  # range
  # column
  # row
  # sheets
# Sheet	            Access and modify spreadsheet sheets.
  # column
  # row
  # name
  # insert
# Range	            Access and modify spreadsheet ranges.
  # note
  # dataValidation
# function printProductInfo() {
  # var sheet = SpreadsheetApp.getActiveSheet();
  # var data = sheet.getDataRange().getValues();
  # for (var i = 0; i < data.length; i++) {
    # Logger.log("Product name: " + data[i][0]);
    # Logger.log("Product number: " + data[i][1]);
  # }
# }
 
 # function addProduct() {
  # var sheet = SpreadsheetApp.getActiveSheet();
  # sheet.appendRow(["Cotton Sweatshirt XL", "css004"]);
# }

