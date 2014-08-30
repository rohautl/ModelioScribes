#---------------------------------------------------------------------------------------
# poi
# from https://wiki.python.org/jython/PoiExample
#---------------------------------------------------------------------------------------

import os


def macro_poitest(scribeexec):
  from java.io import FileOutputStream
  from java.util import Date
  from java.lang import System, Math
  scribeexec.env.setJavaPath([scribeexec.directories['libs.java']+'/poi-3.10.1-20140818.jar'])  
  from org.apache.poi.hssf.usermodel import HSSFWorkbook,HSSFDataFormat,HSSFCellStyle
  from org.apache.poi.hssf.util import HSSFColor
  scribeexec.env.restoreJavaPath()


  startTime = System.currentTimeMillis()

  wb = HSSFWorkbook()
  fileOut = FileOutputStream("C:/tmp/"+"POIOut2.xls")


  # Create 3 sheets
  sheet1 = wb.createSheet("Sheet1")
  sheet2 = wb.createSheet("Sheet2")
  sheet3 = wb.createSheet("Sheet3")
  sheet3 = wb.createSheet("Sheet4")

  # Create a header style
  styleHeader = wb.createCellStyle()
  fontHeader = wb.createFont()
  fontHeader.setBoldweight(2)
  fontHeader.setFontHeightInPoints(14)
  fontHeader.setFontName("Arial")
  styleHeader.setFont(fontHeader)

  # Create a style used for the first column
  style0 = wb.createCellStyle()
  font0 = wb.createFont()
  font0.setColor(HSSFColor.RED.index)
  style0.setFont(font0)


  # Create the style used for dates.
  styleDates = wb.createCellStyle()
  styleDates.setDataFormat(HSSFDataFormat.getBuiltinFormat("m/d/yy h:mm"))


  # create the headers
  rowHeader = sheet1.createRow(1)
  # String value
  cell0 = rowHeader.createCell(0)
  cell0.setCellStyle(styleHeader)
  cell0.setCellValue("Name")


  # numbers
  for i in range(0, 8, 1):
      cell = rowHeader.createCell((i + 1))
      cell.setCellStyle(styleHeader)
      cell.setCellValue("Data " + str( (i + 1)) )


  # Date
  cell10 = rowHeader.createCell(9)
  cell10.setCellValue("Date")
  cell10.setCellStyle(styleHeader)

  for i in range(0, 100, 1):
      # create a new row
      row = sheet1.createRow(i + 2)
      for j in range(0, 10, 1):
          # create each cell
          cell = row.createCell(j)
          # Fill the first column with strings
          if j == 0:
              cell.setCellValue("Product " + str(i))
              cell.setCellStyle(style0)

          # Fill the next 8 columns with numbers.
          elif j < 9:
              cell.setCellValue( (Math.random() * 100))

              # Fill the last column with dates.
          else:
              cell.setCellValue(Date())
              cell.setCellStyle(styleDates)

  # Summary row
  rowSummary = sheet1.createRow(102)
  sumStyle = wb.createCellStyle()
  sumFont = wb.createFont()
  sumFont.setBoldweight( 5)
  sumFont.setFontHeightInPoints(12)
  sumStyle.setFont(sumFont)
  sumStyle.setFillPattern(HSSFCellStyle.FINE_DOTS)
  sumStyle.setFillForegroundColor(HSSFColor.GREEN.index)


  cellSum0 = rowSummary.createCell( 0)
  cellSum0.setCellValue("TOTALS:")
  cellSum0.setCellStyle(sumStyle)


  # numbers
  # B
  cellB = rowSummary.createCell( 1)
  cellB.setCellStyle(sumStyle)
  cellB.setCellFormula("SUM(B3:B102)")

  wb.write(fileOut)
  fileOut.close()

  stopTime = System.currentTimeMillis()
  print 'POI generation took %d ms' %(stopTime - startTime)
  


