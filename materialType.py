import sys
import os
from PyQt5.QtWidgets import QApplication,QWidget,QMessageBox,QListWidgetItem,QTableWidget,QTableWidgetItem,QVBoxLayout
from PyQt5 import uic
from DB.warehouseDB import warehouseDB

class MaterialType(QWidget):
    def __init__(self):
        super().__init__()
        self.InitUI()

    def InitUI(self):
        self.window = uic.loadUi(os.getcwd()+os.sep+r"GUI\materialtype.ui")
        self.window.show()

    def RunProgram(self):
        dataBase=warehouseDB()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MaterialType()
    sys.exit(app.exec_())