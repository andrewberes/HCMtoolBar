"""Opens keynote source file used in this model."""

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
buttonCode = 'Open Keynote File'
logFilePath = r'L:\04 SOFTWARE RESOURCES\Dynamo\zzz.DoNotModify\pyHCMuserLogs'
os.chdir(logFilePath)
f = open(userName + ".txt", "a+")
f.write(buttonCode + "\t" + date +"\n")
f.close()


__author__ = 'Dan Mapes'
__contact__ = 'https://github.com/DMapes'


logger = script.get_logger()


kt = DB.KeynoteTable.GetKeynoteTable(revit.doc)
kt_ref = kt.GetExternalFileReference()
path = DB.ModelPathUtils.ConvertModelPathToUserVisiblePath(
    kt_ref.GetAbsolutePath()
    )

if not path:
    forms.alert('No keynote file is assigned.')
else:
    os.system('start notepad "{0}"'.format(path))
