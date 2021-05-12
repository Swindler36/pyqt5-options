from PyQt5.QtWidgets import QCheckBox

class Checkbox(QCheckBox):
    def __init__(self,value = False):
        super().__init__()
        self.setChecked(value)


