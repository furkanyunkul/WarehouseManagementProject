import sys
import os
from PyQt5.QtWidgets import QApplication,QWidget,QMessageBox,QListWidgetItem,QTableWidget,QTableWidgetItem,QVBoxLayout
from PyQt5 import uic
from DB.warehouseDB import warehouseDB

#warehouse dbden okumuyor

class MaterialMasterDataUI(QWidget):
    def __init__(self):
        super().__init__()
        self.InitUI()
    
    def InitUI(self):
        self.window = uic.loadUi(os.getcwd()+os.sep+r"GUI\materialmasterdata.ui")
        self.window.btnSave.clicked.connect(self.RunProgram)

        self.window.cmbMeaUnit.currentIndexChanged.connect(self.cmbDegisti)

        self.FillingMeasurementUnit()
        self.FillingMaterialType()

        self.window.show()

    def RunProgram(self):
        
        dataBase=warehouseDB()
        
        matNo=self.window.txtMatNo.text
        matName=self.window.txtMatName.text
        meaUnitID="1"
        matTypeID="1"
        cost=self.window.txtCost.text
        
        dataBase.InsertMaterialMasterData("aa","aa",1,2,5)

    def FillingMeasurementUnit(self):
        dataBase=warehouseDB()
        listing=dataBase.ListingMeasurementUnit()
        self.window.cmbMeaUnit.addItem("Choosing","-1")
        print(listing)
        #SORUN BAKILACAK
        
        for meaUniID,meaUnit in listing:
            self.window.cmbMeaUnit.addItem(meaUnit,meaUniID)

    def FillingMaterialType(self):
        dataBase=warehouseDB()
        listing=dataBase.ListingMaterialType()
        self.window.cmbMatType.addItem("Choosing","-1")
        print(listing)
        """
        for matId,matType in listing:
            self.window.cmbMatType.addItem(matType,matId)"""

    def FillingTable(self):
        dataBase=warehouseDB()
        listing=dataBase.ListingMaterialMasterData()
        print(listing)

    def cmbDegisti(self):
        print(self.window.cmbMeaUnit.currentText())
        print(self.window.cmbMeaUnit.currentIndex())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MaterialMasterDataUI()
    sys.exit(app.exec_())

    
