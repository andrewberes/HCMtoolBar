import Autodesk.Revit.DB as DB
from Autodesk.Revit.UI import TaskDialog

import os
import subprocess
import datetime
import pyrevit
import xlrd
import csv


__title__ = 'Import\nExcel'

"""
#button Tracker
now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")
hostapp = pyrevit._HostApplication(__revit__)
userName = hostapp.username
buttonCode = 'import excel'
logFilePath = r'L:\04 SOFTWARE RESOURCES\Dynamo\zzz.DoNotModify\pyHCMuserLogs'
os.chdir(logFilePath)
f = open(userName + ".txt", "a+")
f.write(buttonCode + "\t" + date +"\n")
f.close()
"""
#Read Excel File_________________________________________________________________________________________
"""
# path to the file you want to extract data from
src = 'C:/Users/aberes/Desktop'

os.chdir(src)
book = xlrd.open_workbook('sampleExcel.xlsx')

# select the sheet that the data resides in
work_sheet = book.sheet_by_index(0)

# get the total number of rows
num_rows = work_sheet.nrows
num_col = work_sheet.ncols

Fruit = work_sheet.col(1)
"""


#Trying with CSV

collection = []

os.chdir('C:/Users/aberes/Desktop')
with open('sampleExcel.csv') as f:
	reader = csv.reader(f)
	for row in reader:
		collection.append(row)
		column_Num = len(row)



#Revit Schedule Creation__________________________________________________________________________________
doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument

transaction = DB.Transaction(doc, 'import excel')
transaction.Start()

elemId = DB.ElementId(-1)
sched = DB.ViewSchedule.CreateSchedule(doc, elemId)
sched.Name = "TEST SCHEDULE"


definition = sched.Definition
definition.ShowHeaders = "false"

bodyData = sched.GetTableData().GetSectionData(DB.SectionType.Body)


headerData = sched.GetTableData().GetSectionData(DB.SectionType.Header)

#Bring Excel Data to create Revit Schedule

for i in range(len(collection)):
	headerData.InsertRow(1)

for i in range(column_Num):
	headerData.InsertColumn(1)



headerData.SetColumnWidth(0, .25)
headerData.SetColumnWidth(1, .25)

rowPlace = 0
columnPlace = 0

os.chdir('C:/Users/aberes/Desktop')
with open('sampleExcel.csv') as f:
	reader = csv.reader(f)
	for row in reader:
		headerData.SetCellText(rowPlace, 0, row[0])
		headerData.SetCellText(rowPlace, 1, row[1])


		"""
		if columnPlace == (column_Num - 1):
			columnPlace = 0
		else:
			columnPlace = columnPlace + 1
		"""
		rowPlace = rowPlace + 1



transaction.Commit()