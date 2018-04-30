"""Reloads all linked Revit models."""

from pyrevit import HOST_APP
from pyrevit import revit, DB, UI
from pyrevit.revit import query
from pyrevit import forms
from pyrevit import script
import pyrevit
import os
import datetime

#buttom Tracker
now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")
hostapp = pyrevit._HostApplication(__revit__)
userName = hostapp.username
buttonCode = 'reload links'
logFilePath = r'L:\04 SOFTWARE RESOURCES\Dynamo\zzz.DoNotModify\pyHCMuserLogs'
os.chdir(logFilePath)
f = open(userName + ".txt", "a+")
f.write(buttonCode + "\t" + date +"\n")
f.close()


logger = script.get_logger()


need_tsaxn_dict = [DB.ExternalFileReferenceType.CADLink]


def reload_links(linktype=DB.ExternalFileReferenceType.RevitLink):
    try:
        extrefs = query.get_links(linktype)
        for ref in extrefs:
            logger.debug(ref)

        if extrefs:
            refcount = len(extrefs)
            if refcount > 1:
                selected_extrefs = \
                    forms.SelectFromCheckBoxes.show(
                        extrefs,
                        title='Select Links to Reload',
                        width=500,
                        button_name='Reload',
                        checked_only=True
                        )
                if not selected_extrefs:
                    script.exit()
            elif refcount == 1:
                selected_extrefs = extrefs

            for extref in selected_extrefs:
                print("Reloading...\n\t{0}{1}"
                      .format(str(extref.linktype) + ':', extref.path))
                if linktype in need_tsaxn_dict:
                    with revit.Transaction('Reload Links'):
                        extref.reload()
                else:
                    extref.reload()
    except Exception as load_err:
        logger.debug('Load error: %s' % load_err)
        forms.alert('Model is not saved yet. Can not acquire location.')


linktypes = {'Revit Links': DB.ExternalFileReferenceType.RevitLink}

if HOST_APP.is_newer_than(2017):
    linktypes['CAD Links'] = DB.ExternalFileReferenceType.CADLink
    linktypes['DWF Markup'] = DB.ExternalFileReferenceType.DWFMarkup

if len(linktypes) > 1:
    selected_option = \
        forms.CommandSwitchWindow.show(linktypes.keys(),
                                       message='Select link type:')
else:
    selected_option = 'Revit Links'

if selected_option:
    reload_links(linktypes[selected_option])
