"""DO NOT USE IN CA!
Generates Detail Numbers for current Sheet"""

import sys
from pyrevit.framework import List
from pyrevit import revit, DB, UI
from pyrevit import script
from pyrevit import forms
from Autodesk.Revit.DB import ViewFamilyType, ViewDrafting, Element
from Autodesk.Revit.DB import ViewFamily

import math
import os
import datetime
import pyrevit

__title__ = 'Detail Number\nBy Location'

#buttom Tracker
now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")
hostapp = pyrevit._HostApplication(__revit__)
userName = hostapp.username
buttonCode = 'Detail Number'
logFilePath = r'L:\04 SOFTWARE RESOURCES\Dynamo\zzz.DoNotModify\pyHCMuserLogs'
os.chdir(logFilePath)
f = open(userName + ".txt", "a+")
f.write(buttonCode + "\t" + date +"\n")
f.close()


if __shiftclick__:
    sel_sheets = forms.select_sheets(title='Select Sheets')

if isinstance(revit.activeview, DB.ViewSheet):
	sel_sheets = [revit.activeview]
else:
	forms.alert('Active view must be a sheet.')
	script.exit()

sheetlist = sel_sheets

vportMinX = []
vportMinY = []
vportMinimumPoint = []
minCoord = []
detailNumber = []
dumbDetailNumber = []
newDetailNumber = []
vportOnSheet = []
locationX = []
locationY = []
columnLetters = ('A','B','C','D','E','F','G','H','J','K','L','M',"A")



sheetHeight = 2.5
sheetWidth = 3.5
verticalMargin = ((5 / 8) / 12)
leftMargin = (2.5 / 12)
rightMargin = (4 / 12)
columns = 13
rows = 9

domainX = ((sheetWidth - rightMargin) - leftMargin)
domainY = ((sheetHeight - verticalMargin) - verticalMargin)
divisorX = (domainX / columns)
divisorY = (domainY / rows)


builtInParam = DB.BuiltInParameter.VIEWPORT_DETAIL_NUMBER

with revit.Transaction("Set Detail Number"):
	for sheet in sheetlist:
		counter = int(0)
		for vportid in sheet.GetAllViewports():
			vport = revit.doc.GetElement(vportid)
			
			#This is where i need to filter out the type:Legends from my list of views on the sheet. This if statement is not working
			if vport.Name != "No Title":
				detailNumberParam = vport.get_Parameter(builtInParam)
				detailNumber = detailNumberParam.AsString()
				dumbDetailNumber = detailNumber + str(counter)
				detailNumberParam.Set(dumbDetailNumber)
				counter = counter + 1
				
		for vportid in sheet.GetAllViewports():
			vport = revit.doc.GetElement(vportid)
			if vport.Name != "No Title":
				detailNumberParam = vport.get_Parameter(builtInParam)
				titleMinimumPoint = vport.GetLabelOutline().MinimumPoint
				titleMinX = titleMinimumPoint.X - leftMargin
				locationX = math.floor((titleMinX) / divisorX)
				titleMinY = titleMinimumPoint.Y - verticalMargin
				locationY = (rows - math.floor((titleMinY) / divisorY))
				newDetailNumber = str(int(locationY)) + columnLetters[int(locationX)]
				detailNumberParam.Set(newDetailNumber)