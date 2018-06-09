"""Launch an email to the BIM support form. This is a test of the GitKraken system.
"""

import os
import pyrevit
import datetime

__title__ = 'HCM BIM\nSupport'
__context__ = 'zerodoc'

#buttom Tracker
now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")
hostapp = pyrevit._HostApplication(__revit__)
userName = hostapp.username
buttonCode = 'Support'
logFilePath = 'L:\Dynamo\zzz.DoNotModify\pyHCMuserLogs'
os.chdir(logFilePath)
f = open(userName + ".txt", "a+")
f.write(buttonCode + "\t" + date + "\n")
f.close()

import os
os.startfile('L:\Dynamo\zzz.DoNotModify\supportTicketTemplate.oft - Shortcut')


