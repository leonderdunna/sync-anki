from aqt import mw
from aqt.utils import showInfo, qconnect
from aqt.qt import *

current_new_deck = {"server": "Server", "servername": "Servername", "name": "Deck Name"}


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

    header.setLayout(header_layout)
    return header


def generate_deck_list():
    decks = mw.addonManager.getConfig(__name__)["decks"]

    scroll_area = QScrollArea()
    scroll_area.setWidgetResizable(True)
    list_widget = QWidget()

    list_layout = QBoxLayout(QBoxLayout.Direction(2))

    for deck in decks:
        delete_button = QPushButton("Löschen")

        server = deck["server"]
        servername = deck["servername"]

        qconnect(delete_button.clicked,
                 # python ist komisch. der erste parameter ist komischerweise immer falsch. daher serevername=
                 # servername. das erfüllt keinen aneren
                 # zweck als dafür zu sorgen, dass deck nicht die erste zuweisung innerhalb der lamda funktion ist
                 lambda servername=servername, deck=deck: deleteDeck(deck))

        server_Label = QLabel("Server: " + deck["server"])
        server_name_label = QLabel("Servername: " + deck["servername"])
        deck_name_label = QLabel("Deck: " + deck["name"])

        line = QWidget()
        line_layout = QBoxLayout(QBoxLayout.Direction(0))
        line_layout.addWidget(delete_button)

        line_layout.addWidget(server_Label)
        line_layout.addWidget(server_name_label)
        line_layout.addWidget(deck_name_label)
        line.setLayout(line_layout)
        list_layout.addWidget(line)
    add_widget = QWidget()
    add_layout = QBoxLayout(QBoxLayout.Direction(0))
    add_button = QPushButton("Hinzufügen")

    add_server_input = QLineEdit()
    add_server_input_label = QLabel("Server:")
    add_server_name_input = QLineEdit()
    add_server_name_input_label = QLabel("Servername:")
    add_deck_name_input = QLineEdit()
    add_deck_name_input_label = QLabel("Deck:")
    qconnect(add_button.clicked, lambda: addDeck(add_server_input, add_server_name_input, add_deck_name_input))

    add_layout.addWidget(add_button)
    add_layout.addWidget(add_server_input_label)
    add_layout.addWidget(add_server_input)
    add_layout.addWidget(add_server_name_input_label)
    add_layout.addWidget(add_server_name_input)
    add_layout.addWidget(add_deck_name_input_label)
    add_layout.addWidget(add_deck_name_input)
    add_widget.setLayout(add_layout)
    list_layout.addWidget(add_widget)
    list_widget.setLayout(list_layout)
    list_widget.setLayout(list_layout)
    scroll_area.setWidget(list_widget)
    return scroll_area


def generate_footer():
    footer = QWidget()
    footer_layout = QBoxLayout(QBoxLayout.Direction(0))
    close_button = QPushButton("Schließen")
    qconnect(close_button.clicked, lambda: mw.settings_widget.close())
    footer_layout.addWidget(close_button)
    footer.setLayout(footer_layout)
    return footer


def addDeck(server_input, server_name_input, deck_name_input):
    # Get the current configuration of the add-on
    config = mw.addonManager.getConfig(__name__)
    server = server_input.text()
    server_name = server_name_input.text()
    deck_name = deck_name_input.text()
    # check if any of the input fields is empty
    if server == "" or server_name == "" or deck_name == "":
        showInfo("Error: Please fill all the required fields")
    else:
        # check if the deck already exists
        existing_decks = [d for d in config["decks"] if
                          d["server"] == server and d["servername"] == server_name and d["name"] == deck_name]
        if len(existing_decks) != 0:
            showInfo("Error: This deck already exists")
        else:
            # Create a new deck object with the values from the input fields
            new_deck = {"server": server, "servername": server_name, "name": deck_name}
            # Append the new deck to the list of decks in the configuration
            config["decks"].append(new_deck)
            # Write the updated configuration
            mw.addonManager.writeConfig(__name__, config)
            open_settings_widget()


def deleteDeck(deck):
    config = mw.addonManager.getConfig(__name__)
    decks = config["decks"]

    for i, d in enumerate(decks):
        if d["server"] == deck["server"] and d["servername"] == deck["servername"] and d["name"] == deck["name"]:
            del decks[i]
            break

    config["decks"] = decks
    mw.addonManager.writeConfig(__name__, config)
    open_settings_widget()
