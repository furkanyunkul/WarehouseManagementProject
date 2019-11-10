import sys
import os
from PyQt5.QtWidgets import QApplication,QWidget,QMessageBox,QListWidgetItem,QTableWidget,QTableWidgetItem,QVBoxLayout
from PyQt5 import uic
from DB.warehouseDB import warehouseDB
from datetime import datetime


class MaterialEntry(QWidget):
    def __init__(self):
        super().__init__()
        self.InitUI()

    def InitUI(self):
        self.window = uic.loadUi(os.getcwd()+os.sep+r"GUI\materialentry.ui")
        self.FillingMeasurement()
        self.FillingTable()
        self.FillingMaterilNo()
        self.window.btnSave.clicked.connect(self.RunProgram)
        self.window.tblList.doubleClicked.connect(self.FillingLableTable)

        self.window.show()

    def FillingTable(self):
        dataBase=warehouseDB()
        listing=dataBase.ListingViewMaterialEntry()
        for id,matId,matNo,matName,quan,mUIName,entDate,partyNo,expDate in listing:
            item = QListWidgetItem("{}/{}/{}/{}/{}/{}/{}/{}/{}".format(id,matId,matNo,matName,quan,mUIName,entDate,partyNo,expDate))
            self.window.tblList.addItem(item)

    def FillingLableTable(self):
        gelen=self.window.tblList.currentItem().text().split("/")       
        print(gelen)
        deneme = gelen[0]
        print(deneme)
        self.window.lblMatID.setText(gelen[0])
        self.window.cmbMNo.setCurrentText(gelen[2])
        self.window.txtQuantity.setText(gelen[4])
        self.window.txtParty.setText(gelen[7])
        self.window.cmbMeaUnit.setCurrentText(gelen[5])


    def FillingMeasurement(self):
        dataBase=warehouseDB()
        listing=dataBase.ListingMeasurementUnit()
        self.window.cmbMeaUnit.addItem("Choosing","-1")
        print(listing)
        for mId,mUName in listing:
            self.window.cmbMeaUnit.addItem(mUName,mId)

    def FillingMaterilNo(self):
        dataBase=warehouseDB()
        listing=dataBase.ListingMaterialNo()
        self.window.cmbMNo.addItem("Choosing","-1")
        print(listing)
        for mId,mNo in listing:
            self.window.cmbMNo.addItem(mNo,mId)

    def RunProgram(self):
        dataBase=warehouseDB()
        #current indexte se.ilen ile farklı değer geliyor
        
        
        MId=self.window.cmbMNo.currentIndex()
        MId=str(MId)
        print(MId)
        listing=dataBase.ListingMaterialNo()
        print(dataBase.ListingMaterialNo())
        print(self.window.cmbMNo.currentIndex())
        quan=self.window.txtQuantity.text()
        mUId="1"
        #mUId=self.window.cmbMeaUnit.currentIndex()
        mUId=str(mUId)
        print(mUId)
        
        party=self.window.txtParty.text()
        expDate=self.window.dtExpDate.text()

        answer=QMessageBox.question(self,"SAVING MATERIAL ENTRY","Do you want to save this record",QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if(answer==QMessageBox.Yes):
            if(dataBase.InsertingMaterialEntry(MId,quan,mUId,party,expDate)):
                dataBase.InsertingProcess("7",MId,mUId,quan,party)
                QMessageBox.information(self,"SAVING MATERIAL ENTRY","Saving Successful",QMessageBox.Ok,QMessageBox.Ok)
        elif(answer==QMessageBox.No):
            QMessageBox.information(self,"SAVING MATERIAL ENTRY","Saving Nonsuccessful",QMessageBox.Ok,QMessageBox.Ok)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MaterialEntry()
    sys.exit(app.exec_())