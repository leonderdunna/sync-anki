
from aqt import mw

from aqt.utils import showInfo, qconnect

from aqt.qt import *

import webbrowser
from .settings import open_settings_widget

addon_name = "Sync"
bug_report_url = "https://github.com/leonderdunna/sync-anki/issues"



def opengithub():
    webbrowser.open(bug_report_url)


#
#   Extras
#       Sync
#           Sync-All
#           Einstellungen
#           Fehler Melden
#
# Menü einträge generieren:
menuSync = QMenu(addon_name)
menuEntrySyncAll = QAction("Alles Synchronisieren", mw)
menuEntrySettings = QAction("Einstellungen", mw)
menuEntryReport = QAction("Fehler Melden", mw)

qconnect(menuEntryReport.triggered, opengithub)
qconnect(menuEntrySettings.triggered, open_settings_widget)

menuSync.addAction(menuEntrySyncAll)
menuSync.addAction(menuEntrySettings)
menuSync.addAction(menuEntryReport)

mw.form.menuTools.addMenu(menuSync)
