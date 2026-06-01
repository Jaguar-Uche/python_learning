import requests

from wordslist import easy_words as words
import random
import threading

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class Hangman(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(600,50,700,700)
        self.setStyleSheet("background-color:rgb(51,54,56);")
        self.head_label = QLabel("o",self)
        self.left_torso_label = QLabel("/",self)
        self.center_torso_label = QLabel("|",self)
        self.right_torso_label = QLabel("\\",self)
        self.left_feet_label = QLabel("/",self)
        self.right_feet_label = QLabel("\\",self)
        self.hint_label = QLabel("- - - - -",self)
        self.fail_label = QLabel("",self)
        self.word_description = QLabel("A greeting used when you are playing with people around you so that everybody understands who u are",self)
        self.letter_label = QLabel("Enter a letter:")
        self.letter_input = QLineEdit(self)
        # self.letter_input.setGeometry(0, 100, 50, 50) - This doesn't work here because layout is going to take control of the sizing of this
        self.letter_button = QPushButton("Guess",self)
        self.letter_button.setObjectName("guessButton")
        self.guessed_letters = []
        self.word=""
        self.hint_list =[]
        self.hint_string=""
        self.is_running = True
        self.wrong_guesses = 0
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Hangman")
        self.letter_button.clicked.connect(self.acceptLetter)
        self.fail_label.setFixedSize(500,40)
        self.fail_label.setStyleSheet("background-color:rgb(255,255,255);")
        self.fail_label.setFont(QFont("Arial",10))
        self.fail_label.setAlignment(Qt.AlignCenter)
        # Entire Box Layout
        entire_box = QVBoxLayout()
        entire_box.setContentsMargins(0, 50, 0, 0)
        entire_box.setSpacing(40)  # Optional: better spacing

        # Figure Widget and Layout
        figure_widget = QWidget()

        figure_box = QVBoxLayout()
        figure_box.setSpacing(0)

        # === HEAD: Center it properly ===
        head_box = QHBoxLayout()
        head_box.addStretch()  # Push head to center
        head_box.addWidget(self.head_label)
        head_box.addStretch()  # Push from both sides

        figure_box.addLayout(head_box)

        # === TORSO: Already in HBox, but center the whole row ===
        central_torso_box = QHBoxLayout()
        central_torso_box.addWidget(self.left_torso_label)
        central_torso_box.addWidget(self.center_torso_label)
        central_torso_box.addWidget(self.right_torso_label)
        # No need to setAlignment on the HBox itself if we center the layout below

        # Wrap torso in a centered row
        torso_row = QHBoxLayout()
        torso_row.addStretch()
        torso_row.addLayout(central_torso_box)
        torso_row.addStretch()

        figure_box.addLayout(torso_row)

        # === FEET ===
        feet_box = QHBoxLayout()
        feet_box.addWidget(self.left_feet_label)
        feet_box.addWidget(self.right_feet_label)
        feet_box.setAlignment(Qt.AlignCenter)

        feet_row = QHBoxLayout()
        # feet_row.addStretch()
        feet_row.addLayout(feet_box)

        # feet_row.addStretch()

        figure_box.addLayout(feet_row)
        # Figure complete here, add to widget
        figure_widget.setLayout(figure_box)
        figure_widget.setStyleSheet("background-color:rgb(255, 255, 255);"
                                    "border-radius:15px;")
        figure_widget.setFixedWidth(200)

        figure_center_box = QHBoxLayout()
        figure_center_box.addStretch()
        figure_center_box.addWidget(figure_widget)
        figure_center_box.addStretch()

        entire_box.addLayout(figure_center_box)

        # === Hint, Description, Input ===
        hint_box = QHBoxLayout()
        # hint_box.addStretch()
        hint_box.addWidget(self.hint_label)
        self.hint_label.setStyleSheet("""
            background-color: white;
            border-radius: 15px;
            border: 4px solid #333;
        """)
        # hint_box.addStretch()
        self.hint_label.setFixedSize(500, 80)
        self.hint_label.setAlignment(Qt.AlignCenter)

        fail_box = QHBoxLayout()
        fail_box.addStretch()
        fail_box.addWidget(self.fail_label)
        fail_box.addStretch()

        word_description_box = QHBoxLayout()
        word_description_box.addStretch()
        self.word_description.setAlignment(Qt.AlignCenter)
        self.word_description.setFixedSize(600, 300)
        self.word_description.setWordWrap(True)
        self.word_description.setStyleSheet("background-color:rgb(255, 255, 255);"
                                    "border-radius:5px;")
        word_description_box.addWidget(self.word_description)
        word_description_box.addStretch()

        self.letter_label.setAlignment(Qt.AlignCenter)

        # Add hint and description centered
        entire_box.addLayout(hint_box)
        entire_box.addLayout(fail_box)
        entire_box.addLayout(word_description_box)
        # entire_box.addWidget(self.letter_label)

        # === Input Box: Center the input + button ===
        input_widget = QWidget()
        input_box = QHBoxLayout()
        self.letter_input.setFixedSize(50, 30)  # Reasonable size
        self.letter_input.setAlignment(Qt.AlignCenter)
        self.letter_input.setStyleSheet("background-color:rgb(51,54, 56);"
                                        "color:white")

        self.letter_button.setFixedWidth(80)
        self.letter_button.setStyleSheet("""
            #guessButton {
                background-color: rgb(230, 230, 230);
                border: 3px solid black;
                border-radius: 10px;
            }

            #guessButton:hover {
                background-color: rgb(180, 220, 255);
            }

            #guessButton:pressed {
                background-color: rgb(150, 200, 255);
            }
        """)
        # self.letter_button.setStyleSheet("border:3px solid;"
        #                                 "border-color:rgb(51,54, 56);"
        #                                  "border-radius:10px;")

        input_box.addStretch()
        input_box.addWidget(self.letter_label)
        input_box.addWidget(self.letter_input)
        input_box.addWidget(self.letter_button)
        input_box.addStretch()
        input_widget.setLayout(input_box)
        input_widget.setStyleSheet("background-color:rgb(255, 255, 255);"
                                   "border-radius:5px;")
        input_widget.setFixedWidth(400)
        entire_box.addWidget(input_widget, alignment=Qt.AlignCenter)

        # === Final centering of all rows ===
        entire_box.addStretch()  # Push everything up a bit if needed
        self.setLayout(entire_box)

        # === Font & Size Settings (move here or keep in init) ===
        font = QFont("Arial", 36, QFont.Bold)  # Monospace helps alignment
        self.head_label.setFont(font)
        self.left_torso_label.setFont(font)
        self.center_torso_label.setFont(font)
        self.right_torso_label.setFont(font)
        self.left_feet_label.setFont(font)
        self.right_feet_label.setFont(font)

        self.hint_label.setFont(QFont('Arial', 30))
        self.word_description.setFont(QFont('Arial', 15))
        self.letter_label.setFont(QFont('Arial', 15))
        self.letter_button.setFont(QFont('Arial', 15))
        self.letter_button.setFixedWidth(100)
        self.letter_input.setFont(QFont('Arial', 15))
        self.startGame()

    def startGame(self):
        self.word = random.choice(words)
        self.getWordMeaning(self.word)
        self.hint_list = ["_"] * len(self.word)  # <-- keep this as a list
        # Display version
        self.hint_string = " ".join(self.hint_list)
        self.set_hint()
        # word_meaning = threading.Thread(target= self.getWordMeaning, args=(self.word,))
        # word_meaning.start()


    def getWordMeaning(self, word):
        print("Word :"+ word)
        # Make a request to the api and then get the description of the worddd
        url = f"https://freedictionaryapi.com/api/v1/entries/en/{word}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            definition = data['entries'][0]['senses'][0]['definition']
            self.word_description.setText(definition)
        except requests.exceptions.HTTPError as httperror:
            # httperror is when the status code is not 200
            match response.status_code:
                case 400:
                    self.fail_label.setText("Bad Request:\nPlease Check Your input")
                    print("Bad Request:\nPlease Check Your input")
                case 401:
                    self.fail_label.setText("Unauthorized:\nInvalid API Key")
                    print("Unauthorized:\nInvalid API Key")
                case 403:
                    self.display_error("Forbidden:\nAccess Denied")
                    print("Forbidden:\nAccess Denied")
                case 404:
                    self.fail_label.setText("Not Found:\nCity Not Found")
                    print("Not Found:\nCity Not Found")
                case 500:
                    self.fail_label.setText("Internal Server Error:\nPlease Try Again Later")
                    print("Internal Server Error:\nPlease Try Again Later")
                case 502:
                    self.fail_label.setText("Bad Gateway:\nnvalid response from the server")
                    print("Bad Gateway:\nnvalid response from the server")
                case 503:
                    self.fail_label.setText("Service Unavailable:\nServer is down")
                    print("Service Unavailable:\nServer is down")
                case 504:
                    self.fail_label.setText("Gateway Timeout:\nNo Response from the server")
                    print("Gateway Timeout:\nNo Response from the server")
                case _:
                    self.fail_label.setText(f"HTTP Error Occured:\n{httperror}")
                    print(f"HTTP Error Occured:\n{httperror}")

        except requests.exceptions.ConnectionError:
            print("Connection Error:\nCheck Your Internet Connection")
            self.word_description.setText("Connection Error:\nCheck Your Internet Connection")
        except requests.exceptions.Timeout:
            print("Timeout Error:\nThe Request timed out")
            self.word_description.setText("Timeout Error:\nThe Request timed out")
        except requests.exceptions.TooManyRedirects:
            print("Too Many Redirects:\nCheck the url")
            self.word_description.setText("Too Many Redirects:\nCheck the url")
        except requests.exceptions.RequestException as req_error:
            # Network problems or invalid url
            print(f"Request Error:\n{req_error}")
            self.word_description.setText(f"Request Error:\n{req_error}")


    def set_hint(self):
        self.hint_label.setText(f"{self.hint_string.capitalize()}")

    def acceptLetter(self):
        # Accept letter then check it across the word
        letter = self.letter_input.text()
        self.letter_input.setText("")
        if len(letter) and letter.isalpha() == 1:
            if letter in self.guessed_letters:
                self.fail_label.setText(f"You have already guessed {letter}")
            else:
                self.guessed_letters.append(letter)
                if letter in self.word:
                    for i in range(len(self.word)):
                        if self.word[i]  == letter:
                            self.hint_list[i] = letter
                            self.hint_string = " ".join(self.hint_list)
                        self.fail_label.setText(f"{letter} has been guessed successfully")
                    if "_" not in self.hint_string:
                        self.fail_label.setText("You have won the game")
                        self.letter_button.setDisabled(True)
                        self.is_running = False
                        self.word = ""
                        self.hint_list = []
                        self.hint_string = ""

                else:
                    self.wrong_guesses += 1
                    self.fail_label.setText(f"You have guessed {letter} incorrectly")
                    if self.wrong_guesses >= 6:
                        self.fail_label.setText(f"You have lost the game")
                        print(self.word)
                        self.hint_string = self.word
                        self.set_hint()
                        self.letter_button.setDisabled(True)
                        self.is_running=False
                        self.word = ""
                        self.hint_list = []
                        self.hint_string = ""
                    self.print_hangman()
        else:
            self.fail_label.setText(f"Input a single letter")

        self.set_hint()

    def print_hangman(self):
        match self.wrong_guesses:
            case 1:
                self.right_feet_label.hide()
            case 2:
                self.left_feet_label.setText("")
            case 3:
                self.right_torso_label.setText("")
            case 4:
                self.left_torso_label.setText("")
            case 5:
                self.center_torso_label.setText("")
            case 6:
                self.head_label.setText("")
            case _:
                pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    hangman = Hangman()
    hangman.show()
    sys.exit(app.exec_())