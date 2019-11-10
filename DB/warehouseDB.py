from DB.DB import DBTools
import os

class warehouseDB(DBTools):
    def __init__(self,):
        super(warehouseDB,self).__init__(os.getcwd()+os.sep+r"DB\WarehouseManagement.db")
        #self.TABLE="MATERIAL_MASTER_DATA"

    def InsertMaterialMasterData(self,matNo,matName,meaUnitID,matTypeID,cost):
         print(self.Inserting(TABLE=self.TABLE,COLUMN=["MATERIAL_NO","MATERIAL_NAME","MEASUREMENT_UNIT_ID","MATERIAL_TYPE_ID","COST"]
,VALUE=["'"+matNo+"'","'"+matName+"'",meaUnitID,matTypeID,cost]))

    def ListingMeasurementUnit(self):
        return self.Listing(TABLE="MEASUREMENT_UNIT",COLUMN=["ID","MEASUREMENT_UNIT_NAME"],ORDER="MEASUREMENT_UNIT_NAME")

    

    def ListingMaterialType(self):
        print(self.Listing(TABLE="MATERIAL_TYPE",COLUMN=["ID","MATERIAL_TYPE_NAME"],CONDITION="1=1"))

    def ListingMaterialMasterData(self):
        print(self.Listing(TABLE="MATERIAL_MASTER_DATA",COLUMN=["ID","MATERIAL_NO","MATERIAL_NAME","MEASUREMENT_UNIT_ID","MATERIAL_TYPE_ID","COST"],CONDITION="1=1"))

    def ListingWarehouseName(self):
        return self.Listing(TABLE="WAREHOUSE",COLUMN=["ID","WAREHOUSE_NAME"],ORDER="WAREHOUSE_NAME")

    def ListingMaterialEntry(self):
         return self.Listing(TABLE="MATERIAL_ENTRY",COLUMN=["ID","MATERIAL_ID","QUANTITY","MEASUREMENT_UNIT_ID","ENTRY_DATE","PARTY_NO","EXPIRATION_DATE"],ORDER="ENTRY_DATE")


    #material_masterdan veri gelmiyor
    def ListingMaterialNo(self):
        return self.Listing(TABLE="MATERIALS_MASTER_DATA",COLUMN=["ID","MATERIAL_NO"],ORDER="ID" )

    def ListingMaterialNoWithContion(self,mNo):
        return self.Listing(TABLE="MATERIALS_MASTER_DATA",COLUMN=["ID"],WHERE="MATERIAL_NO="+"'"+mNo+"'" )


    def ListingMaterialNo_deneme(self,mNo):
        self.DBConnect()
        query="SELECT CAST(ID AS VARCHAR) AS ID FROM MATERIAL_MASTER_DATA WHERE MATERIAL_NO=mNo ORDER BY MATERIAL_NO"
        print(query)
        self.cur.execute(query)
        return query

    def ListingViewMaterialEntry(self):
        return self.Listing(TABLE="VW_MATERIAL_ENTRY",COLUMN=["ID","MATERIAL_ID","MATERIAL_NO","MATERIAL_NAME","QUANTITY","MEASUREMENT_UNIT_NAME","ENTRY_DATE","PARTY_NO","EXPIRATION_DATE"],ORDER="ENTRY_DATE DESC")

    def InsertingMaterialEntry(self,matId,quan,mUId,partyNo,expDate):
        return self.Inserting(TABLE="MATERIAL_ENTRY",COLUMN=["MATERIAL_ID","QUANTITY","MEASUREMENT_UNIT_ID","PARTY_NO","EXPIRATION_DATE"],
        VALUE=["'"+matId+"'","'"+quan+"'","'"+mUId+"'","'"+partyNo+"'","'"+expDate+"'"]) 

    def InsertingProcess(self,processId,matId,mUId,quan,partyNo):
        return self.Inserting(TABLE="WAREHOUSE_PROCESS",COLUMN=["PROCESS_ID","MATERIAL_ID","QUANTITY","MEASUREMENT_ID","PARTY_NO"],
        VALUE=["'"+processId+"'","'"+matId+"'","'"+mUId+"'","'"+quan+"'","'"+partyNo+"'"])

    def InsertingWarehouseQuantity(self,locId,matId,quan,mUId,partyNo,expDate):
        print(self.Inserting(TABLE="WAREHOUSE_QUANTITY",COLUMN=["LOCATION_ID","MATERIAL_ID","QUANTITY","MEASUREMENT_UNIT_ID","PARTY_NO","EXPIRATION_DATE"],
        VALUE=["'"+locId+"'","'"+matId+"'","'"+quan+"'","'"+mUId+"'","'"+partyNo+"'","'"+expDate+"'"]))

    def ListingViewQuality(self):
        return self.Listing(TABLE="VW_QUALITY",COLUMN=["ID","WAREHOUSE_NAME","LOCATION_ID","LOCATION_NAME","MATERIAL_ID","MATERIAL_NO","MATERIAL_NAME","QUANTITY","MEASUREMENT_UNIT_ID","MEASUREMENT_UNIT_NAME","PARTY_NO","EXPIRATION_DATE"],ORDER="ID DESC")

    def UpdatingWarehouseQuantity(self,id,locationId):
        self.DBConnect()
        query="UPDATE WAREHOUSE_QUANTITY SET LOCATION_ID={} WHERE ID={}".format(locationId,id)
        print(query)
        self.cur.execute(query)
        self.db.commit()

    def ListingLocationGeneral(self):
        return self.Listing(TABLE="VM_LOCATIONS",COLUMN=["ID","LOCATION_NAME"],CONDITION="WAREHOUSE_ID<>0",ORDER="LOCATION_NAME")

    
    def ListingLocation(self,wName="WAREHOUSE"):
        return self.Listing(TABLE="VM_LOCATIONS",COLUMN=["ID","LOCATION_NAME"],CONDITION="WAREHOUSE_NAME="+"'"+wName+"'",ORDER="LOCATION_NAME")

    def ListingLocationWithCondtion(self,wName,locClicked):
        return self.Listing(TABLE="VM_LOCATIONS",COLUMN=["ID","LOCATION_NAME"],CONDITION="WAREHOUSE_NAME="+"'"+wName+"'"+" AND LOCATION_NAME<>"+"'"+locClicked+"'",ORDER="LOCATION_NAME")

    def ListingLocation_V2(self,selected):
        return self.Listing(TABLE="VM_LOCATIONS",COLUMN=["ID"],CONDITION="LOCATION_NAME="+"'"+selected+"'",ORDER="LOCATION_NAME")

    def ListingWareHouseEntry(self):
        return self.Listing(TABLE="VW_WAREHOUSE_ENTRY",COLUMN=["ID","WAREHOUSE_NAME","LOCATION_ID","LOCATION_NAME","MATERIAL_ID","MATERIAL_NO","MATERIAL_NAME","QUANTITY","MEASUREMENT_UNIT_ID","MEASUREMENT_UNIT_NAME","PARTY_NO","EXPIRATION_DATE"],ORDER="ID DESC")

    def Locations(self,listingLog):
        return self.Listing(TABLE="VM_LOCATIONS",COLUMN=["VARCHAR_ID","LOCATION_NAME"],CONDITION="LOCATION_NAME="+"'"+listingLog+"'",ORDER="LOCATION_NAME")

    def UpdatingWarehouseQuantityForScraping(self,id,isOk):
        self.DBConnect()
        query="UPDATE WAREHOUSE_QUANTITY SET IS_OK={} WHERE ID={}".format(isOk,id)
        print(query)
        self.cur.execute(query)
        self.db.commit()

    def InsertingScrap(self,mNo,quan,partyNo,mUId,id):
        return self.Inserting(TABLE="SCRAP_MATERIAL",COLUMN=["MATERIAL_NO","QUANTITY","PARTY_NO","MEASUREMENT_UNIT_ID","MATERIAL_ENTRY_ID"],
        VALUE=["'"+mNo+"'","'"+quan+"'","'"+partyNo+"'",mUId,id])

    def ListingViewWarehouse(self):
        return self.Listing(TABLE="VM_WAREHOUSE",COLUMN=["ID","WAREHOUSE_NAME","LOCATION_ID","LOCATION_NAME","MATERIAL_ID","MATERIAL_NO","MATERIAL_NAME","QUANTITY","MEASUREMENT_UNIT_ID","MEASUREMENT_UNIT_NAME","PARTY_NO","EXPIRATION_DATE"],ORDER="LOCATION_ID")

    def UpdatingWarehouseQuantityWithQuantity(self,id,quantity):
        self.DBConnect()
        query="UPDATE WAREHOUSE_QUANTITY SET QUANTITY={} WHERE ID={}".format(quantity,id)
        print(query)
        self.cur.execute(query)
        self.db.commit()

    def UpdatingWarehouseQuantityWithQuantityIsOk(self,id,quantity,isOk):
        self.DBConnect()
        query="UPDATE WAREHOUSE_QUANTITY SET QUANTITY={},IS_OK={} WHERE ID={} ".format(quantity,isOk,id)
        print(query)
        self.cur.execute(query)
        self.db.commit()

    def ListingWarehouseProcess(self):
        return self.Listing(TABLE="VM_WAREHOUSE_PROCESS",COLUMN=["ID","PROCESS_ID","MATERIAL_ID","MATERIAL_NAME","MATERIAL_NO","QUANTITY","MEASUREMENT_ID","MEASUREMENT_UNIT_NAME","PROCESSING_DATE"],ORDER="PROCESSING_DATE")











    