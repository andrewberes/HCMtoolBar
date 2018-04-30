"""Reload keynote source file used in this model."""

import os
import pyrevit
import datetime

from pyrevit import revit, DB, UI
from pyrevit import script
from pyrevit import forms

#buttom Tracker
now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")
hostapp = pyrevit._HostApplication(__revit__)
userName = hostapp.username
buttonCode = 'Reload Keynote File'
logFilePath = r'L:\04 SOFTWARE RESOURCES\Dynamo\zzz.DoNotModify\pyHCMuserLogs'
os.chdir(logFilePath)
f = open(userName + ".txt", "a+")
f.write(buttonCode + "\t" + date +"\n")
f.close()



kt = DB.KeynoteTable.GetKeynoteTable(revit.doc)

t = DB.Transaction(revit.doc)
t.Start('Keynote Reload')
try:
    result = kt.Reload(None)
    t.Commit()

except:
    t.RollBack()

forms.alert('Keynote Reloading : {}'.format(result))
# result can be 'Success', 'ResourceAlreadyCurrent' or 'Failure'

