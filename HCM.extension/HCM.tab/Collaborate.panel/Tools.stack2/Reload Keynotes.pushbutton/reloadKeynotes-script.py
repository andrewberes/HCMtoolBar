"""Reload keynote source file used in this model."""


from pyrevit import revit, DB, UI
from pyrevit import script
from pyrevit import forms



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

