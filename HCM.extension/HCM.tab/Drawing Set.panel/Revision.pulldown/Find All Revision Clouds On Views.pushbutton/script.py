from pyrevit import revit, DB
import pyrevit
import os
import datetime

#buttom Tracker
now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")
hostapp = pyrevit._HostApplication(__revit__)
userName = hostapp.username
buttonCode = 'find revision clouds on views'
logFilePath = r'L:\04 SOFTWARE RESOURCES\Dynamo\zzz.DoNotModify\pyHCMuserLogs'
os.chdir(logFilePath)
f = open(userName + ".txt", "a+")
f.write(buttonCode + "\t" + date +"\n")
f.close()


__doc__ = 'Lists all revision clouds in this model that have been '\
          'placed on a view and not on sheet.'

revs = DB.FilteredElementCollector(revit.doc)\
         .OfCategory(DB.BuiltInCategory.OST_RevisionClouds)\
         .WhereElementIsNotElementType()

for rev in revs:
    parent = revit.doc.GetElement(rev.OwnerViewId)
    if isinstance(parent, DB.ViewSheet):
        continue
    else:
        print('REV#: {0}\t\tID: {2}\t\tON VIEW: {1}'
              .format(revit.doc.GetElement(rev.RevisionId).RevisionNumber,
                      parent.ViewName,
                      rev.Id))

print('\nSEARCH COMPLETED.')
