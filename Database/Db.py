import pymongo 
import datetime

# MongoDB database
class db_interface():
    def __init__(self):
        # Connects to database 
        self.conn=pymongo.MongoClient()
        print ("Connected Successfully")
        # Creates a database named "WRPS_DATA" if no database exists prior. If a database with the same name already exists, then it will ignore it
        self.db=self.conn.WRPS_DATA
        # creates a collection(similar to table in relational database)
        self.collection=self.db.WRPS_collection
    
    # Inserts data into the database
    def put(self,data):
        self.collection.insert(data)
        #self.collection.drop()
        #db.WRPS_collection.find()
        #for element in self.collection.find():
            #self.collection.update({'$set':{'Incident_date':datetime()}})
        #for result in self.collection.find():
            #print (result)
        #print (self.collection.count())




    
