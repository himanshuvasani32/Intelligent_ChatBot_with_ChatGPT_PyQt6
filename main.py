from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton
import sys
from backend import ChatBot
import threading


class ChatMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.chatbot = ChatBot()

        self.setMinimumSize(700, 450)

        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 320)
        self.chat_area.setReadOnly(True)

        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 340, 480, 40)
        self.input_field.returnPressed.connect(self.send_message)

        self.send_button = QPushButton("Send", self)
        self.send_button.setGeometry(500, 340, 100, 40)
        self.send_button.clicked.connect(self.send_message)

        self.show()

    def send_message(self):
        user_input = self.input_field.text().strip()
        self.chat_area.append(f"<p style='color: #333333'>Me: {user_input}</p>")
        self.input_field.clear()

        thread = threading.Thread(target=self.get_bot_response, args=(user_input, ))
        thread.start()

    def get_bot_response(self):
        response = self.chatbot.get_response(user_input)
        self.chat_area.append(f"<p style='color: #333333; background-color: #E9E9E9'>bot: {response}</p>")


app = QApplication(sys.argv)
chat_window = ChatMainWindow()
sys.exit(app.exec())
