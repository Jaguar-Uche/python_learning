import sys

from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton,QWidget,QHBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.setGeometry(700,300,500,500)
        # You don't need this because we are using a layout manager
        self.button1 = QPushButton("#1")
        # No need to add to self since we are using a layout manager
        self.button2 = QPushButton("#2")
        self.button3 = QPushButton("#3")

        self.initUI()

    def initUI(self):
        # Remember you can't add layout managers directly, so you create a central widget
        central_widget = QWidget()
        # add the central manager to the main window
        self.setCentralWidget(central_widget)
        # And everything you want to add to the layout managers
        hbox = QHBoxLayout()
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        # Then add the layout manager to the central widget
        central_widget.setLayout(hbox)

        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")
        # Makes it easier to use setStyleSheet without self.button1 you can use the objectName

        # Instead of individually, we apply the styles to the main window
        self.setStyleSheet("""
            QPushButton{
            font-size:40px;
            font-family:Arial;
            padding:15px 75px;
            margin:25px;
            border:3px solid;
            border-radius:15px;
            }
            QPushButton#button1{
                background-color:#ff4747;
                
            }
             QPushButton#button2{
                background-color:hsl(122, 100%, 64%);
                
            }
             QPushButton#button3{
                background-color:blue;
                
            }
            QPushButton#button1:hover{
                background-color:#ffadad;
                
            }
             QPushButton#button2:hover{
                background-color:hsl(122, 100%, 84%);
                
            }
             QPushButton#button3:hover{
                background-color:hsl(204,100%, 84%);
            }
        """)
        # """ is used for very long string
        print()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())