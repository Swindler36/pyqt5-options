from PyQt5.QtWidgets import QVBoxLayout, QDialog, QApplication
import sys
from scripts.tabs import Tab
from scripts.config import OPTION_CONFIG

app = QApplication(sys.argv)

class OptionWindow(QDialog):
    def __init__(self,opt_config):
        super().__init__()
        self.title = "deneme"
        self.resize(600,600)
        self.config = {}
        self.setWindowTitle(self.title)

        layout = QVBoxLayout()

        tabs = Tab(opt_config,self.config)
        layout.addWidget(tabs.tabs)


        self.setLayout(layout)
        




ex = OptionWindow(OPTION_CONFIG)

ex.show()

sys.exit(app.exec_())

