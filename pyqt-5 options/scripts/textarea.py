from PyQt5.QtWidgets import QPlainTextEdit

class TextArea(QPlainTextEdit):
    def __init__(self,placeholder = "",value = ""):
        super().__init__()
        self.setPlainText(value)
        self.setPlaceholderText(placeholder)


