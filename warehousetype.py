import sys
import os
from PyQt5.QtWidgets import QApplication,QWidget,QMessageBox,QListWidgetItem,QTableWidget,QTableWidgetItem,QVBoxLayout
from PyQt5 import uic
from DB.warehouseDB import warehouseDB

class WarehouseType(QWidget):
    def __init__(self):
        super().__init__()
        self.InitUI()

    def InitUI(self):
        self.window = uic.loadUi(os.getcwd()+os.sep+r"GUI\warehousetype.ui")
        self.FillinWareHouseName()
        self.window.show()

    def RunProgram(self):
        dataBase=warehouseDB()


    def FillinWareHouseName(self):
        dataBase=warehouseDB()
        listing=dataBase.ListingWarehouseName()
        self.window.cmbWName.addItem("Choosing","-1")
        print(listing)
        for wId,wname in listing:
            self.window.cmbWName.addItem(wname,wId)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = WarehouseType()
    sys.exit(app.exec_())