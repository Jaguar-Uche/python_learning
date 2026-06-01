import sys

from PyQt5.QtWidgets import QApplication,QMainWindow,QRadioButton,QButtonGroup

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)
        self.radio1 = QRadioButton("Visa",self)
        self.radio2 = QRadioButton("MasterCard",self)
        self.radio3 = QRadioButton("Gift Card",self)
        self.radio4 = QRadioButton("In Store", self)
        self.radio5 = QRadioButton("Online", self)
        # By default, all of them are in the same group so selecting any one deselects the other
        self.button_group1 = QButtonGroup(self)
        self.button_group2 = QButtonGroup(self)

        self.initUI()

    def initUI(self):
        self.radio1.setGeometry(0,0,300,50)
        self.radio2.setGeometry(0,50,300,50)
        self.radio3.setGeometry(0,100,300,50)
        self.radio4.setGeometry(0, 150, 300, 50)
        self.radio5.setGeometry(0, 200, 300, 50)


        self.setStyleSheet("QRadioButton{"
                           "font-size:40px;"
                           "font-family:Arial;"
                           "padding:10px"
                                        "}")
        # This is used for setting the styleSheet of a group of somethings - QRadioButtons here

        # First radio button group

        self.button_group1.addButton(self.radio1)
        self.button_group1.addButton(self.radio2)
        self.button_group1.addButton(self.radio3)

        # We have separated them into different radio button groups
        self.button_group2.addButton(self.radio4)
        self.button_group2.addButton(self.radio5)

        # Now you can only select one from a radio button group

        self.radio1.toggled.connect(self.radio_button_clicked)
        self.radio2.toggled.connect(self.radio_button_clicked)
        self.radio3.toggled.connect(self.radio_button_clicked)
        self.radio4.toggled.connect(self.radio_button_clicked)
        self.radio5.toggled.connect(self.radio_button_clicked)


    def radio_button_clicked(self):
        radio_button = self.sender()
        # self.sender() returns the widget that sent the signal
        if radio_button.isChecked():
            print(f"{radio_button.text()} is selected")
        elif not radio_button.isChecked():
            print(f"{radio_button.text()} just got deselected")
        #     This shows that when you select a new one, it deselects the old one before selectu=ing the new one
        print()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())