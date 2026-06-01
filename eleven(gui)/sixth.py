
# Checkboxes

import sys

from PyQt5.QtWidgets import QApplication,QMainWindow, QCheckBox
from PyQt5.QtCore import Qt
# This contains non gui classes relevant to PyQt5 applications

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)
        self.checkbox = QCheckBox("Do You Like Food?",self)
        # first argument is name and the second is where you are applying it or putting it inside
        self.initUI()

    def initUI(self):
        self.checkbox.setGeometry(10, 0, 500, 100)
        self.checkbox.setStyleSheet("font-size:30px;"
                                    "font-family:Arial;"
                                    )
        # self.checkbox.setChecked(True)-This makes the checkbox checked by default when the window loads
        self.checkbox.stateChanged.connect(self.checkbox_changed)


    def checkbox_changed(self,state):
        # print(state) State of 0 means unchecked and state of 2 means checked
        if state == Qt.Checked:
            print("You like food")
        elif state == Qt.Unchecked:
            print("You don't like food")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())