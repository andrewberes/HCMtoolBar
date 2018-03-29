from Autodesk.Revit.DB import ViewSchedule, ViewScheduleExportOptions
from Autodesk.Revit.DB import ExportColumnHeaders, ExportTextQualifier
from Autodesk.Revit.DB import BuiltInCategory, ViewSchedule
from Autodesk.Revit.UI import TaskDialog

import os
import subprocess
import datetime
import pyrevit

#buttom Tracker
now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")
hostapp = pyrevit._HostApplication(__revit__)
userName = hostapp.username
buttonCode = 'open excel'
logFilePath = 'L:\Dynamo\zzz.DoNotModify\pyHCMuserLogs'
os.chdir(logFilePath)
f = open(userName + ".txt", "a+")
f.write(buttonCode + "\t" + date +"\n")
f.close()





doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument

desktop = os.path.expandvars('%temp%\\')
vseop = ViewScheduleExportOptions()

selected_ids = uidoc.Selection.GetElementIds()

if not selected_ids.Count:
    '''If nothing is selected, use Active View'''
    selected_ids=[ doc.ActiveView.Id ]

for element_id in selected_ids:
    element = doc.GetElement(element_id)
    if not isinstance(element, ViewSchedule):
        print('No schedule in Selection. Skipping...')
        continue

    filename = "".join(x for x in element.ViewName if x not in ['*']) + '.txt'
    element.Export(desktop, filename, vseop)

    print('EXPORTED: {0}\n      TO: {1}\n'.format(element.ViewName, filename))
    EXCEL = r"C:\Program Files (x86)\Microsoft Office\root\Office16\EXCEL.EXE"
    if os.path.exists(EXCEL):
        print('Excel Found. Trying to open...')
        print('Filename is: ', filename)
        try:
            full_filepath = os.path.join(desktop, filename)
            os.system('start excel \"{path}\"'.format(path=full_filepath))
        except:
            print('Sorry, something failed:')
            print('Filepath: {}'.filename)
            print('EXCEL Path: {}'.format(EXCEL))
    else:
        print('Could not find excel. EXCEL: {}'.format(EXCEL))
print('Done')
