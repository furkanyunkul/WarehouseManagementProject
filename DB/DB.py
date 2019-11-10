import sqlite3 as sql

class DBTools():
    def __init__(self,address=""):
        self.address=address

    def DBConnect(self):
        self.db=sql.connect(self.address)
        self.cur=self.db.cursor()

    def Listing(self,**kwargs):
        try:
            self.DBConnect()
            columns=""
            values=""
            conditions=""
            order=""

            for key,value in kwargs.items():
                if key=="TABLE":
                    table=value
                elif key=="COLUMN":
                    for item in value:
                        columns=columns+item+","
                    columns=columns.rstrip(",")
                elif key=="CONDITION":
                    conditions=value
                elif key=="ORDER":
                    order=value

            if not conditions:
                conditions="1=1"
            if not order:
                order="ORDER BY ID"
            query="SELECT {} FROM {} WHERE {} ORDER BY {}".format(columns,table,conditions,order)
            print(query)
            self.cur.execute(query)
            return self.cur.fetchall()
        except:
            return None
        finally:
            self.db.close()

    def Inserting(self,**kwargs):
        try:
            self.DBConnect()
            columns=""
            values=""

            for key,value in kwargs.items():
                if key=="TABLE":
                    table=value
                elif key=="COLUMN":
                    for item in value:
                        columns=columns+item+","
                    columns=columns.rstrip(",")
                elif key=="VALUE":
                    for item in value:
                        values=values+item+","
                    values=values.rstrip(",")
            query="INSERT INTO {} ({}) VALUES ({})".format(table,columns,values)
            print(query)
            self.cur.execute(query)
            self.db.commit()
            return True
        except Exception as mistake:
            print(mistake)
            return False
        finally:
            self.db.close()

    def Updating(self,**kwargs):
        try:
            self.DBConnect()
            columns=[]
            values=[]
            conditions=""
            for key,value in kwargs.items():
                if key=="TABLE":
                    table=value
                elif key=="COLUMN":
                    columns=value
                elif key=="VALUE":
                    values=value
                elif key=="CONDITION":
                    conditions=value
            
            updates=""
            
            for i in range(0,len(columns)):
                updates=updates+columns[i]+" = "+str(values[i])+","
            updates=updates.rstrip(",")

            query="UPDATE {} SET {} WHERE {}".format(table,updates,conditions)
            print(query)
            self.cur.execute(query)
            self.db.commit()
            return True          
        except Exception as mistake :
            print(mistake)
            return False
        finally:
            self.db.close()

    def Deleting(self,**kwargs):
        try:
            self.DBConnect()
            conditions=""
            for key,value in kwargs.items():
                if key=="TABLE":
                    table=value
                elif key=="CONDITION":
                    conditions=value
            query="DELETE FROM {} WHERE {}".format(table,conditions)
            self.cur.execute(query)
            self.db.commit()
            return True
        except Exception as mistake:
            print(mistake)
            return False
        finally:
            self.db.close()
            

        
