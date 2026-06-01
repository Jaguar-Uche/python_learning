import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QLabel,QWidget,QVBoxLayout,QHBoxLayout,QGridLayout
from PyQt5.QtGui import QIcon,QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First GUI program")
        self.setGeometry(700, 300, 500, 500)
        self.setWindowIcon(QIcon("favicon.svg"))
        self.initUI()

    #     MainWindows widgets have a specific design and layout structure that is normally incompatible with layout manager
    #  So we create a widget, add layout manager to it and add the widget to the layout manager

    def initUI(self):
        # Separates anything that has to do with the user interface into this area
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        label1 = QLabel("#1",self)
        label2 = QLabel("#2", self)
        label3 = QLabel("#3", self)
        label4 = QLabel("#4", self)
        label5 = QLabel("#5", self)

        label1.setStyleSheet("background-color:red;")
        label2.setStyleSheet("background-color:yellow;")
        label3.setStyleSheet("background-color:blue;")
        label4.setStyleSheet("background-color:green;")
        label5.setStyleSheet("background-color:purple;")

        # Normally, they are overlapping so we need a layout manager to handle it

        # vbox = QVBoxLayout()
        # vbox.addWidget(label1)
        # vbox.addWidget(label2)
        # vbox.addWidget(label3)
        # vbox.addWidget(label4)
        # vbox.addWidget(label5)
        #
        # central_widget.setLayout(vbox)

        # hbox = QHBoxLayout()
        # hbox.addWidget(label1)
        # hbox.addWidget(label2)
        # hbox.addWidget(label3)
        # hbox.addWidget(label4)
        # hbox.addWidget(label5)
        #
        # central_widget.setLayout(hbox) - horizontal layout

        gbox = QGridLayout()
        # gbox.addwidget(label,row, column) 0 based indexing ohhh
        gbox.addWidget(label1, 0,0)
        gbox.addWidget(label2, 0,1)
        gbox.addWidget(label3, 1, 0)
        gbox.addWidget(label4 ,1, 1)
        gbox.addWidget(label5 ,2,2)

        central_widget.setLayout(gbox)
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()