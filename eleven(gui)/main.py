
# PyQt5 introduction

import sys
# This is for variables used and maintained by the python interpreter

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

# The widgets from the PyQt5 have Q in front of them to differentiate them from the other ones

class MainWindow(QMainWindow):
    #  It inherits from the QMainWindow and we can customize how we display it to users
    def __init__(self):
        super().__init__()
        # If there is an argument to pass into the QMainWindow, u pass it in here
        self.setWindowTitle("My First GUI program")
        self.setGeometry(700, 300, 500, 500)
        # self.setGeometry(x, y, width, height)
        self.setWindowIcon(QIcon("favicon.svg"))
        # This is the image it shows at the top side and the image it shows on the taskbar


def main():
    app = QApplication(sys.argv)
    #  We create an app with system.argv system arguments
    # Allows PyQt to use command line arguments intended for it. we aren't using command line here so you can run
    # app = QApplication([]) instead
    window = MainWindow()
    # with just this, the window would not show cause the default behaviour of a window is to hide
    window.show()
    # This only appears for a brief second
    sys.exit(app.exec_())
    # sys.exit() ensures a clean exit of our code
    # app.exec_() handles button click and user input events


if __name__ == '__main__':
    main()