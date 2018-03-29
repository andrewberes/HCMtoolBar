"""Lists all sheets revised under any revision."""

from pyrevit import revit, DB
from pyrevit import script
import pyrevit
import os
import datetime

#buttom Tracker
now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")
hostapp = pyrevit._HostApplication(__revit__)
userName = hostapp.username
buttonCode = 'find all revised sheets'
logFilePath = 'L:\Dynamo\zzz.DoNotModify\pyHCMuserLogs'
os.chdir(logFilePath)
f = open(userName + ".txt", "a+")
f.write(buttonCode + "\t" + date +"\n")
f.close()

output = script.get_output()

output.print_md('**LIST OF REVISIONS:**')


revs = DB.FilteredElementCollector(revit.doc)\
         .OfCategory(DB.BuiltInCategory.OST_Revisions)\
         .WhereElementIsNotElementType()

for rev in revs:
    print('{0}\tREV#: {1}\tDATE: {2}\tTYPE:{3}\tDESC: {4}'
          .format(rev.SequenceNumber,
                  str(rev.RevisionNumber).ljust(5),
                  str(rev.RevisionDate).ljust(10),
                  str(rev.NumberType.ToString()).ljust(15),
                  rev.Description))

output.print_md('*****\n\n\n###REVISED SHEETS:\n')

sheetsnotsorted = DB.FilteredElementCollector(revit.doc)\
                    .OfCategory(DB.BuiltInCategory.OST_Sheets)\
                    .WhereElementIsNotElementType()\
                    .ToElements()

sheets = sorted(sheetsnotsorted, key=lambda x: x.SheetNumber)

for sht in sheets:
    revs = sht.GetAllRevisionIds()
    if len(revs) > 0:
        print('{}\t{}\t{}'
              .format(output.linkify(sht.Id),
                      sht.LookupParameter('Sheet Number').AsString(),
                      sht.LookupParameter('Sheet Name').AsString()))

        for rev in revs:
            rev = revit.doc.GetElement(rev)
            print('\tREV#: {0}\t\tDATE: {1}\t\tDESC:{2}'
                  .format(rev.RevisionNumber,
                          rev.RevisionDate,
                          rev.Description))
