"""Launch an email to the BIM support form.
"""
import os
import pyrevit
import datetime


__title__ = 'Resources'
__context__ = 'zerodoc'

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

import os
os.startfile('I:\Revit Standards\Shortcuts')


