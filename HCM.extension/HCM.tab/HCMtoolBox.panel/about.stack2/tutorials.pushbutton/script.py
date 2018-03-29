"""Opens the HCM intranet home page."""

import os
import pyrevit
import datetime

__context__ = 'zerodoc'
__title__ = 'Videos'

#buttom Tracker
now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")
hostapp = pyrevit._HostApplication(__revit__)
userName = hostapp.username
buttonCode = __title__
logFilePath = 'L:\Dynamo\zzz.DoNotModify\pyHCMuserLogs'
os.chdir(logFilePath)
f = open(userName + ".txt", "a+")
f.write(buttonCode + "\t" + date +"\n")
f.close()

from pyrevit import script
script.open_url('http://web/bim/default.aspx')
