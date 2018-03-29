"""Sets the revision visibility parameter to None for all revisions."""

from pyrevit import revit, DB

import pyrevit
import os
import datetime

#buttom Tracker
now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")
hostapp = pyrevit._HostApplication(__revit__)
userName = hostapp.username
buttonCode = 'turn off all revisions'
logFilePath = 'L:\Dynamo\zzz.DoNotModify\pyHCMuserLogs'
os.chdir(logFilePath)
f = open(userName + ".txt", "a+")
f.write(buttonCode + "\t" + date +"\n")
f.close()

revs = DB.FilteredElementCollector(revit.doc)\
         .OfCategory(DB.BuiltInCategory.OST_Revisions)\
         .WhereElementIsNotElementType()

with revit.Transaction('Turn off Revisions'):
    for rev in revs:
        rev.Visibility = DB.RevisionVisibility.Hidden
