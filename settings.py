#settings.py

from aqt import mw
from aqt.utils import showInfo, qconnect
from aqt.qt import *


def open_settings_widget():
    mw.settings_widget = settings_widget = QWidget()
    settings_layout = QBoxLayout(QBoxLayout.Direction(2))
    settings_layout.addWidget(generateheader())
    settings_layout.addWidget(generate_deck_list())
    settings_layout.addWidget(generate_footer())
    settings_widget.setLayout(settings_layout)
    settings_widget.show()


def generateheader():
    header = QWidget()
    header_layout = QBoxLayout(QBoxLayout.Direction(0))

    header_layout.addWidget(QLabel("Sync-Einstellungen"))

    sync_button = QPushButton("Synchronisieren")
    header_layout.addWidget(sync_button)
    info_button = QPushButton("Info")
    report_button = QPushButton("Fehler Melden")
    header_layout.addWidget(info_button)
    header_layout.addWidget(report_button)
    header.setLayout(header_layout)
    return header


def generate_deck_list():
    decks = mw.addonManager.getConfig(__name__)["decks"]
    print("↓↓↓↓↓↓↓↓↓↓")
    print(decks)

    list = QWidget()
    list_layout = QBoxLayout(QBoxLayout.Direction(2))
    for deck in decks:
        delete_button = QPushButton("Löschen")
        edit_button = QPushButton("Bearbeiten")
        server_Label = QLabel("Server: " + deck["server"])
        server_name_label = QLabel("Servername: " + deck["servername"])
        deck_name_label = QLabel("Deck: " + deck["name"])

        line = QWidget()
        line_layout = QBoxLayout(QBoxLayout.Direction(0))
        line_layout.addWidget(delete_button)
        line_layout.addWidget(edit_button)
        line_layout.addWidget(server_Label)
        line_layout.addWidget(server_name_label)
        line_layout.addWidget(deck_name_label)
        line.setLayout(line_layout)
        list_layout.addWidget(line)
    add_widget = QWidget()
    add_layout = QBoxLayout(QBoxLayout.Direction(0))
    add_button = QPushButton("Hinzufügen")

    add_server_input = QLineEdit("Server: ")
    add_server_name_input = QLineEdit("Servername: ")
    add_deck_name_input = QLineEdit("Deck: ")
    add_layout.addWidget(add_button)
    add_layout.addWidget(add_server_input)
    add_layout.addWidget(add_server_name_input)
    add_layout.addWidget(add_deck_name_input)
    add_widget.setLayout(add_layout)
    list_layout.addWidget(add_widget)
    list.setLayout(list_layout)
    return list


def generate_footer():
    footer = QWidget()
    footer_layout = QBoxLayout(QBoxLayout.Direction(0))
    save_button = QPushButton("Speichern")
    exit_button = QPushButton("Schließen")
    footer_layout.addWidget(save_button)
    footer_layout.addWidget(exit_button)
    footer.setLayout(footer_layout)
    return footer
