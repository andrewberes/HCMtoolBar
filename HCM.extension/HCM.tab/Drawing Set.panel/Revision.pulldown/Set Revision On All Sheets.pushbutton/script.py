from pyrevit.framework import List
from pyrevit import revit, DB
from pyrevit import forms
import os
import datetime
import pyrevit

#buttom Tracker
now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")
hostapp = pyrevit._HostApplication(__revit__)
userName = hostapp.username
buttonCode = 'set revision on all sheets'
logFilePath = 'L:\Dynamo\zzz.DoNotModify\pyHCMuserLogs'
os.chdir(logFilePath)
f = open(userName + ".txt", "a+")
f.write(buttonCode + "\t" + date +"\n")
f.close()


__doc__ = 'Select a revision from the list of revisions and '\
          'this script set that revision on all sheets in the '\
          'model as an additional revision.'


def set_rev_on_sheets(revision_element, sheets=None):
    if not sheets:
        # collect data
        sheets = DB.FilteredElementCollector(revit.doc)\
                   .OfCategory(DB.BuiltInCategory.OST_Sheets)\
                   .WhereElementIsNotElementType()\
                   .ToElements()

    affectedsheets = []
    with revit.Transaction('Set Revision on Sheets'):
        for s in sheets:
            revs = list(s.GetAdditionalRevisionIds())
            revs.append(revision_element.Id)
            s.SetAdditionalRevisionIds(List[DB.ElementId](revs))
            affectedsheets.append(s)

    if len(affectedsheets) > 0:
        print('SELECTED REVISION ADDED TO THESE SHEETS:')
        print('-' * 100)
        for s in affectedsheets:
            snum = s.LookupParameter('Sheet Number').AsString().rjust(10)
            sname = s.LookupParameter('Sheet Name').AsString().ljust(50)
            print('NUMBER: {0}   NAME:{1}'.format(snum, sname))


revision = forms.select_revisions(button_name='Select Revision',
                                  multiselect=False)

sheets = forms.select_sheets(button_name='Set Revision')

if revision and sheets:
    set_rev_on_sheets(revision, sheets)
