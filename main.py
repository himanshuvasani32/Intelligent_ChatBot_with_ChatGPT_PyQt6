from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton
import sys


class ChatMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(700, 450)

        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 320)
        self.chat_area.setReadOnly(True)

        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 340, 480, 40)

        self.send_button = QPushButton("Send", self)
        self.send_button.setGeometry(500, 340, 100, 40)

        self.show()


app = QApplication(sys.argv)
chat_window = ChatMainWindow()
sys.exit(app.exec())
