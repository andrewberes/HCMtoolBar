"""Exports the current view to a 600DPI PNG image."""

from pyrevit.framework import Forms
from pyrevit import revit, DB

import os
import pyrevit
import datetime

__title__ = 'Capture\nWindow'

#buttom Tracker
now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")
hostapp = pyrevit._HostApplication(__revit__)
userName = hostapp.username
buttonCode = 'capture window'
logFilePath = r'L:\04 SOFTWARE RESOURCES\Dynamo\zzz.DoNotModify\pyHCMuserLogs'
os.chdir(logFilePath)
f = open(userName + ".txt", "a+")
f.write(buttonCode + "\t" + date +"\n")
f.close()


# collect file location from user
dialog = Forms.SaveFileDialog()
dialog.Title = 'Export current view as JPG'
dialog.Filter = 'JPG files (*.JPG)|*.JPG'

if dialog.ShowDialog() == Forms.DialogResult.OK:
    # set up the export options
    options = DB.ImageExportOptions()
    options.ExportRange = DB.ExportRange.VisibleRegionOfCurrentView
    options.FilePath = dialog.FileName
    #options.HLRandWFViewsFileType = DB.ImageFileType.PNG
    options.ImageResolution = DB.ImageResolution.DPI_600
    options.ZoomType = DB.ZoomFitType.Zoom
    #options.ShadowViewsFileType = DB.ImageFileType.PNG

    revit.doc.ExportImage(options)
