from PyQt5.QtWidgets import QSlider
from PyQt5.QtCore import Qt 

class Slider(QSlider):
    def __init__(self,range = (0,100),value = 15):
        super().__init__(Qt.Horizontal)
        self.setValue(value)
        self.setRange(range[0],range[1])

   

