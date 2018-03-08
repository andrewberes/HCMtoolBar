"""DO NOT USE IN CA!
Generates Detail Numbers for current Sheet"""

import sys

from pyrevit import revit, DB, UI
from pyrevit import script
from pyrevit import forms

import math

__title__ = 'Detail Number\nBy Location'


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
		for vportid in sheet.GetAllViewports():
			vport = revit.doc.GetElement(vportid)
			detailNumberParam = vport.get_Parameter(builtInParam)
			detailNumber = detailNumberParam.AsString()
			dumbDetailNumber = detailNumber + 'dup'
			detailNumberParam.Set(dumbDetailNumber)
			detailNumberParam = vport.get_Parameter(builtInParam)
			titleMinimumPoint = vport.GetLabelOutline().MinimumPoint
			titleMinX = titleMinimumPoint.X - leftMargin
			locationX = math.floor((titleMinX) / divisorX)
			titleMinY = titleMinimumPoint.Y - verticalMargin
			locationY = (rows - math.floor((titleMinY) / divisorY))
			newDetailNumber = str(int(locationY)) + columnLetters[int(locationX)]
			detailNumberParam.Set(newDetailNumber)

