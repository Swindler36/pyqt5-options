from PyQt5.QtWidgets import QLineEdit

class Text(QLineEdit):
    def __init__(self,placeholder = "",value = ""):
        super().__init__()
        self.setText(value)
        self.setPlaceholderText(placeholder)

