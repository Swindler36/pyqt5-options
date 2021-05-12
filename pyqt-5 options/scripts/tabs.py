from PyQt5.QtWidgets import QFormLayout, QLabel, QWidget, QHBoxLayout, QPushButton, QDialog, QApplication, QTabWidget, QVBoxLayout
from .text import Text
from .textarea import TextArea
from .select import Select
from .checkbox import Checkbox
from .color_picker import ColorPicker
from .slider import Slider


from PyQt5.QtGui import QIcon


class Tab():
    def __init__(self,config,field_config):

        self.tabs = QTabWidget()
        self.opts = field_config

        for i in config:
            if "children" in i:

                ws = i["children"]
                tab_widget = QWidget()
                tab_layout = QFormLayout()
                tab_widget.setLayout(tab_layout)

                for w in ws:
                    value = ""
                    help = ""
                    # value
                    if "value" in w:
                        value = w["value"]

                    # help
                    if "help" in w:
                        help = w["help"]

                    if w["type"] == "text":
                        field = Text(help,value)

                    elif w["type"] == "textarea":
                        field = TextArea(help,value)
                    
                    elif w["type"] == "select":
                        field = Select(w["data"],value)

                    elif w["type"] == "checkbox":
                        field = Checkbox(value)

                    elif w["type"] == "color":
                        field = ColorPicker(value)

                    elif w["type"] == "slider":
                        field = Slider(w["range"],value)
                      


                    tab_layout.addRow( QLabel(w["label"]), field )
                    self.opts[ i["label"] + "_" + w["label"] ] = field
        
                if "icon" in i:
                    self.tabs.addTab(tab_widget,QIcon( i["icon"] ),i["label"])
                else:
                    self.tabs.addTab(tab_widget,i["label"])

            



