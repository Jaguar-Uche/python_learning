import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QLabel
from PyQt5.QtGui import QIcon,QPixmap
# Qpixmap is for providing functionality on images

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First GUI program")
        self.setGeometry(700, 300, 500, 500)
        self.setWindowIcon(QIcon("favicon.svg"))

        label = QLabel(self)
        label.setGeometry(0,0,250,250)

        pixmap = QPixmap("favicon.svg")
        label.setPixmap(pixmap)
        # The image doesn't scale according to the size of the label so u enable it
        label.setScaledContents(True)
        # Makes image the same size as the label

        # label.setGeometry(self.width()-label.width(),
        #                   self.height() - label.height(),
        #                   label.width(),
        #                   label.height())
        # This sets it at the bottom right corner. ie width of the app - width of label to give top right

        label.setGeometry((self.width() - label.width()) //2,
                          (self.height() - label.height())//2,
                          label.width(),
                          label.height())

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()