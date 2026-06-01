import sys

from PyQt5.QtWidgets import QApplication, QMainWindow,QPushButton,QLabel
# Push Button Widgets


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.button = QPushButton("Click Me", self)
        self.label = QLabel("Hello", self)
        self.initUI()

    def initUI(self):
        # When creating widgets, you want to prefix it with self, else you would create a local variable to this function
        # and you cant access it else where
        # button = QPushButton("Click Me", self)
        # Also,create the variable in the constructor class so u carry the self.button to the constructor place
        self.button.setGeometry(150, 200, 200, 100)
        self.label.setGeometry(150, 300, 200, 100)
        self.button.setStyleSheet("font-size:30px;")
        self.label.setStyleSheet("font-size:50px;")
        # We have to set a signal - When a widget is interacted with like event listeners
        self.button.clicked.connect(self.on_click)
        # This disables the button after clicking on it

    def on_click(self):
        print("Button Clicked")
        # button.setText("Clicked") doesn't work cause button is local to initUI
        self.label.setText("Goodbye")
        self.button.setDisabled(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())