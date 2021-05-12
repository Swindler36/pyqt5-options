from PyQt5.QtWidgets import QColorDialog, QPushButton
from PyQt5.QtGui import QColor

class ColorPicker(QPushButton):
    def __init__(self,value = [255,255,255,255]):
        super().__init__('Open color dialog')
        self.rgb = value
        self.setToolTip('Opens color dialog')
        self.move(10,10)
        self.clicked.connect(self.openColorDialog)

    def openColorDialog(self):
        self.color = QColorDialog.getColor()

        if not self.color.isValid():
            self.color = False
        else:
            self.rgb = self.color.getRgb()
            self.setStyleSheet("background-color: rgba({},{},{},{})".format( self.rgb[0], self.rgb[1], self.rgb[2], self.rgb[3]))

        


