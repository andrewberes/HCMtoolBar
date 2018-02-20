"""DO NOT USE IN CA!
Generates Detail Numbers for current Sheet"""

import sys
from revitutils import selection, doc, uidoc, curview, Action
from Autodesk.Revit.UI import *
from Autodesk.Revit.DB import *
import math

__title__ = 'Detail Number\nBy Location'

doc = __revit__.ActiveUIDocument.Document

filteredlist = []
sheetlist = []

"""
print("Please do not use this tool in C.A. as it will re-coordinate all referenced on the sheet, thus causing conflicts with 'Revisions'")
"""

if selection.is_empty:
    if isinstance(curview, ViewSheet):
        sheetlist.append(curview)
else:
    for sel_view in selection:
        if isinstance(sel_view, ViewSheet):
            sheetlist.append(sel_view)

if not sheetlist:
    TaskDialog.Show('pyrevit','You must have at least one sheet selected or active view must be a sheet.')
    sys.exit()


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
columnLetters = ('A','B','C','D','E','F','G','H','J','K','L','M')



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


builtInParam = BuiltInParameter.VIEWPORT_DETAIL_NUMBER

t = Transaction(doc, "Set dupDetail Number")
t.Start()
for sheet in sheetlist:
	for vportid in sheet.GetAllViewports():
		vport = doc.GetElement(vportid)
		detailNumberParam = vport.get_Parameter(builtInParam)
		detailNumber = detailNumberParam.AsString()
		dumbDetailNumber = detailNumber + 'dup'
		detailNumberParam.Set(dumbDetailNumber)
t.Commit()

t = Transaction(doc, "Set Detail Number")
t.Start()
for sheet in sheetlist:
	for vportid in sheet.GetAllViewports():
		vport = doc.GetElement(vportid)
		detailNumberParam = vport.get_Parameter(builtInParam)
		vportMinimumPoint = vport.GetBoxOutline().MinimumPoint
		vportMinX = vportMinimumPoint.X - leftMargin
		locationX = math.floor((vportMinX) / divisorX)
		vportMinY = vportMinimumPoint.Y - verticalMargin
		locationY = (rows - math.floor((vportMinY) / divisorY))
		
		newDetailNumber = str(int(locationY)) + columnLetters[int(locationX)]
		detailNumberParam.Set(newDetailNumber)
t.Commit()

