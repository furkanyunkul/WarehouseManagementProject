import sys
import os
from PyQt5.QtWidgets import QApplication,QWidget,QMessageBox,QListWidgetItem,QTableWidget,QTableWidgetItem,QVBoxLayout
from PyQt5 import uic
from DB.warehouseDB import warehouseDB

class Quality(QWidget):
    def __init__(self):
        super().__init__()
        self.InitUI()

    def InitUI(self):
        self.window = uic.loadUi(os.getcwd()+os.sep+r"GUI\quality.ui")
        self.FillingTable()
        self.window.tblList.doubleClicked.connect(self.RunProgram)
        self.secim
        self.window.show()


    
    def FillingTable(self):
        dataBase=warehouseDB()
        listing=dataBase.ListingViewQuality()
        
        for id,wName,locId,locName,MıD,mNo,mName,quan,mUId,mUName,partyNo,expDate in listing:
            item=QListWidgetItem("{}/{}/{}/{}/{}/{}/{}/{}/{}/{}/{}/{}".format(id,wName,locId,locName,MıD,mNo,mName,quan,mUId,mUName,partyNo,expDate))
            self.window.tblList.addItem(item)

    def RunProgram(self):
        dataBase=warehouseDB()
        answer=QMessageBox.question(self,"QUESTION",'Do you want to take quality for this record ?',QMessageBox.Yes | QMessageBox.No)
        if(answer==QMessageBox.Yes):
            print("a")
            #print(listing)
            gelen=self.window.tblList.currentItem().text().split("/")       
            print(gelen)
            #deneme = gelen[0]
            #y=int(deneme)
            processId='2'
            mId=gelen[4]
            quan=gelen[7]
            mUId=gelen[8]
            partyNo=gelen[10]
            id=gelen[0]
            locationId=gelen[2]
            dataBase.InsertingProcess(processId,mId,quan,mUId,partyNo)
            locationId='346' #quality id
            dataBase.UpdatingWarehouseQuantity(id,locationId)
            self.window.tblList.clear()
            self.FillingTable()
            

        elif(answer==QMessageBox.No):
            print("Yok")

    def secim(self):
        dataBase=warehouseDB()
        gelen=self.window.tblList.currentItem().text().split("/")

        print(gelen)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Quality()
    sys.exit(app.exec_())