from pyrevit import revit, DB

import os
import datetime
import pyrevit

#buttom Tracker
now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")
hostapp = pyrevit._HostApplication(__revit__)
userName = hostapp.username
buttonCode = 'find sheets with selected revision'
logFilePath = r'L:\04 SOFTWARE RESOURCES\Dynamo\zzz.DoNotModify\pyHCMuserLogs'
os.chdir(logFilePath)
f = open(userName + ".txt", "a+")
f.write(buttonCode + "\t" + date +"\n")
f.close()

__doc__ = 'Select a revision cloud and this tool will list all '\
          'the sheets revised under the same revision.'

selection = revit.get_selection()

selectedrevs = []
hasSelectedRevision = False
multipleRevs = False

for s in selection:
    if isinstance(s, DB.RevisionCloud):
        selectedrevs.append(s.RevisionId.IntegerValue)

if len(selectedrevs) > 1:
    multipleRevs = True

print('REVISED SHEETS:\n\nNAME\tNUMBER\n' + '-'*70)

sheetsnotsorted = DB.FilteredElementCollector(revit.doc)\
                    .OfCategory(DB.BuiltInCategory.OST_Sheets)\
                    .WhereElementIsNotElementType()\
                    .ToElements()

sheets = sorted(sheetsnotsorted, key=lambda x: x.SheetNumber)

for s in sheets:
    hasSelectedRevision = False
    revs = s.GetAllRevisionIds()
    revIds = [x.IntegerValue for x in revs]
    for sr in selectedrevs:
        if sr in revIds:
            hasSelectedRevision = True
    if hasSelectedRevision:
        print('{0}\t{1}'.format(s.LookupParameter('Sheet Number').AsString(),
                                s.LookupParameter('Sheet Name').AsString()))

        if multipleRevs:
            for rev in revs:
                rev = revit.doc.GetElement(rev)
                print('\tREV#: {0}\t\tDATE: {1}\t\tDESC:{2}'
                      .format(rev.RevisionNumber,
                              rev.RevisionDate,
                              rev.Description))
