from PyQt5.QtWidgets import QComboBox

class Select(QComboBox):
    def __init__(self,data = [],value = ""):
        super().__init__()
        self.addItems(data)
        if value in data:
            self.setCurrentIndex( data.index( value ) )
        self.setPlaceholderText("-------")

        
