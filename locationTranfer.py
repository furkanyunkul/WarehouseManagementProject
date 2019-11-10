import sys
import os
from PyQt5.QtWidgets import QApplication,QWidget,QMessageBox,QListWidgetItem,QTableWidget,QTableWidgetItem,QVBoxLayout
from PyQt5 import uic
from DB.warehouseDB import warehouseDB

class LocationTransfer(QWidget):
    def __init__(self):
        super().__init__()
        self.InitUI()
        
    def InitUI(self):
        self.window = uic.loadUi(os.getcwd()+os.sep+r"GUI\locationtransfer.ui")
        self.FillingTable()
        self.window.tblList.doubleClicked.connect(self.FillingLableTable)
        self.window.btnSave.clicked.connect(self.RunProgram)

        self.window.show()



    def FillingTable(self):
        dataBase=warehouseDB()
        listing=dataBase.ListingViewWarehouse()
        
        for id,wName,locId,locName,MıD,mNo,mName,quan,mUId,mUName,partyNo,expDate in listing:
            item=QListWidgetItem("{}/{}/{}/{}/{}/{}/{}/{}/{}/{}/{}/{}".format(id,wName,locId,locName,MıD,mNo,mName,quan,mUId,mUName,partyNo,expDate))
            self.window.tblList.addItem(item) 

    def FillingLableTable(self):
        dataBase=warehouseDB()

        gelen=self.window.tblList.currentItem().text().split("/") 
        print(gelen)     
        
        self.window.lblMatID.setText(gelen[0])
        self.window.lblLocNo.setText(gelen[3])
        self.window.lblMNo.setText(gelen[5])
        self.window.lblQuantity.setText(gelen[7])
        self.window.lblMUnit.setText(gelen[9])
        self.window.lblParty.setText(gelen[10])
        self.window.lblExDate.setText(gelen[11])

        wName="WAREHOUSE"
        locClicked=str(gelen[3])
        listing=dataBase.ListingLocationWithCondtion(wName,locClicked)
        self.window.cmbLocNo.addItem("Choosing","-1")
        #print(listing)
        for lId,lName in listing:
            self.window.cmbLocNo.addItem(lName,lId)
    
    def RunProgram(self):
        dataBase=warehouseDB()
        answer=QMessageBox.question(self,"LOCATION TRANSFER",'Do you want to tranfer for this record ?',QMessageBox.Yes | QMessageBox.No)
        if(answer==QMessageBox.Yes):

            gelen=self.window.tblList.currentItem().text().split("/")
            processId='8'
            mId=gelen[4]
            quan=gelen[7]
            mUId=gelen[8]
            partyNo=gelen[10]
            expDate=gelen[11]
            id=gelen[0]
            quanNew=self.window.txtQuantity.text()
            locName=self.window.cmbLocNo.currentText()
            locId=str(dataBase.ListingLocation_V2 (locName)[0][0])   
            isOk=0

            quanUpdate=int(quan)-int(quanNew)
            if(quanNew>quan):
                QMessageBox.Warning(self,"LOCATION TRANSFER","Quantity updated is bigger than quantity",QMessageBox.Ok,QMessageBox.Ok)

            else:
                dataBase.InsertingProcess(processId,mId,quan,mUId,partyNo)
                dataBase.InsertingWarehouseQuantity(locId,mId,quanNew,mUId,partyNo,expDate)  
                if(quanUpdate==0):
                    dataBase.UpdatingWarehouseQuantityWithQuantityIsOk(id,quanUpdate,isOk)   
                else:      
                    dataBase.UpdatingWarehouseQuantityWithQuantity(id,quanUpdate)
                QMessageBox.information(self,"LOCATION TRANSFER","This transfer is successful",QMessageBox.Ok,QMessageBox.Ok)
                self.window.tblList.clear()
                self.FillingTable()



        elif (answer==QMessageBox.No):
            QMessageBox.information(self,"LOCATION TRANSFER","This transfer is unsuccessful",QMessageBox.Ok,QMessageBox.Ok)





    #VALUE=["'"+locId+"'","'"+matId+"'","'"+quan+"'","'"+mUId+"'","'"+partyNo+"'","'"+expDate+"'"]))




#                VALUE=["'"+locId+"'","'"+matId+"'","'"+quan+"'","'"+mUId+"'","'"+partyNo+"'","'"+expDate+"'"]))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = LocationTransfer()
    sys.exit(app.exec_())