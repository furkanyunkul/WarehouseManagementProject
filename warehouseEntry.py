import sys
import os
from PyQt5.QtWidgets import QApplication,QWidget,QMessageBox,QListWidgetItem,QTableWidget,QTableWidgetItem,QVBoxLayout
from PyQt5 import uic
from DB.warehouseDB import warehouseDB

class WarehouseEntry(QWidget):
    def __init__(self):
        super().__init__()
        self.InitUI()

    def InitUI(self):
        self.window = uic.loadUi(os.getcwd()+os.sep+r"GUI\warehouseentry.ui")
        self.FillingLocaiton()
        self.FillingTable()
        self.window.tblList.doubleClicked.connect(self.FillingLableTable)
        self.window.btnSave.clicked.connect(self.TakingWarehouse)
        self.window.btnScrap.clicked.connect(self.TakingScraping)

        self.window.show()

    def FillingLocaiton(self):
        dataBase=warehouseDB()
        listing=dataBase.ListingLocation()
        self.window.cmbLocNo.addItem("Choosing","-1")
        #print(listing)
        for lId,lName in listing:
            self.window.cmbLocNo.addItem(lName,lId)

    def FillingTable(self):
        dataBase=warehouseDB()
        listing=dataBase.ListingWareHouseEntry()
        
        for id,wName,locId,locName,MıD,mNo,mName,quan,mUId,mUName,partyNo,expDate in listing:
            item=QListWidgetItem("{}/{}/{}/{}/{}/{}/{}/{}/{}/{}/{}/{}".format(id,wName,locId,locName,MıD,mNo,mName,quan,mUId,mUName,partyNo,expDate))
            self.window.tblList.addItem(item)        

    def FillingLableTable(self):
        gelen=self.window.tblList.currentItem().text().split("/") 
        #print(gelen)     
        self.window.lblMatID.setText(gelen[0])
        self.window.lblMNo.setText(gelen[5])
        self.window.txtQuantity.setText(gelen[7])
        self.window.lblMUnit.setText(gelen[9])
        self.window.lblParty.setText(gelen[10])
        self.window.lblExDate.setText(gelen[11])
    
    def TakingWarehouse(self):
        dataBase=warehouseDB()
        answer=QMessageBox.question(self,"QUESTION",'Do you want to take warehouse for this record ?',QMessageBox.Yes | QMessageBox.No)
        if(answer==QMessageBox.Yes):
            gelen=self.window.tblList.currentItem().text().split("/")       
            print(gelen)
            processId='1'
            mId=gelen[4]
            quan=gelen[7]
            mUId=gelen[8]
            partyNo=gelen[10]
            id=gelen[0]

            dataBase.InsertingProcess(processId,mId,quan,mUId,partyNo)

            locationname=self.window.cmbLocNo.currentText()
            print(locationname)
            listingLog=locationname
            locations=dataBase.Locations(listingLog)
            for lId,lName in locations:
                self.window.cmbLocNo.addItem(lId,lName)
            print(locations)
            locationId=locations[0][0]
            print(str(locationId))

            dataBase.UpdatingWarehouseQuantity(id,locationId)

            QMessageBox.information(self,"TAKING WAREHOUSE","This record is successful",QMessageBox.Ok,QMessageBox.Ok)
            self.window.tblList.clear()
            self.FillingTable()

        elif (answer==QMessageBox.No):
            QMessageBox.information(self,"TAKING WAREHOUSE","This record is unsuccessful",QMessageBox.Ok,QMessageBox.Ok)

    def TakingScraping(self):
        dataBase=warehouseDB()
        answer=QMessageBox.question(self,"QUESTION",'Do you want to scrap this record ?',QMessageBox.Yes | QMessageBox.No)
        if(answer==QMessageBox.Yes):
    
            gelen=self.window.tblList.currentItem().text().split("/")       
            print(gelen)
            processId='5'
            mId=gelen[4]
            quan=gelen[7]
            mUId=gelen[8]
            partyNo=gelen[10]
            id=gelen[0]
            mNo=gelen[5]
            isOk=0
            

            dataBase.InsertingProcess(processId,mId,quan,mUId,partyNo)
            dataBase.UpdatingWarehouseQuantityForScraping(id,isOk)
            dataBase.InsertingScrap(mNo,quan,partyNo,mUId,id)

            QMessageBox.information(self,"SCRAPING","Scraping is successful",QMessageBox.Ok,QMessageBox.Ok)
            self.window.tblList.clear()

            self.FillingTable()

        elif(answer==QMessageBox.Np):
            QMessageBox.information(self,"SCRAPING","Scraping is not successful",QMessageBox.Ok,QMessageBox.Ok)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = WarehouseEntry()
    sys.exit(app.exec_())
