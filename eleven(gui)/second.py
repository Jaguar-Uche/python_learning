import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QLabel
# The QLabel label class is used to create label widgets that display text or images
from PyQt5.QtGui import QIcon,QFont
# QFont is for fonts
from PyQt5.QtCore import Qt
# for alignments

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First GUI program")
        self.setGeometry(700, 300, 500, 500)
        self.setWindowIcon(QIcon("favicon.svg"))

        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 30))
        label.setGeometry(0,0,500,300)
        label.setStyleSheet("color:blue;"
                            "background-color:red;"
                            "font-weight:bold;"
                            "font-style:italic;"
                            "text-decoration:underline")
        # label.setAlignment(Qt.AlignTop) - To align your text vertically to the top
        # label.setAlignment(Qt.AlignBottom) - To align Vertically Bottom
        # label.setAlignment(Qt.AlignVCenter) - To align Vertically to the center

        # label.setAlignment(Qt.AlignRight) - To align horizontally to the right
        # label.setAlignment(Qt.AlignHCenter) - To align horizontally in the center
        # label.setAlignment(Qt.AlignLeft) - To align to the left

        # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) - Horizontal center and top vertical

        label.setAlignment(Qt.AlignCenter)
        # Aligns text to the center vertically and horizontally

        # Accepts css like properties ending in semicolon


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()