"""Basic information regarding the Hord Coplan Macht custom Revit toolbar.
"""
import os
import pyrevit
import datetime

__title__ = 'Info'
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



print('Welcome to the HCM toolBox.')
print('\n')* 2
print('Developed by the Automation Group at HCM.')
print('\n')*2
print('This effort reflects our desire to streamline workflows and generate in house solutions to technological bottle necks.')
print('\n')*2
print('As a task force within the Design Technology Committee, the Automation Group leverages comutational logics to solve Architectural problems')
print('\n')* 2
print('The purpose of this set of tools is to help EVERYONE document faster, and more efficently - ')
print('ultimatly, leaving more time for GREAT DESIGN.')

