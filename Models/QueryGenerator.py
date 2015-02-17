import re
from Db import db_interface
from datetime import datetime
import pymongo
from bson.son import SON
from bson.code import Code

# returns information of all incidents in required time interval
class QueryGenerator():
    def __init__(self,start_date,end_date,start_time,end_time):
        mod_start_date=start_date+' '+start_time
        mod_end_date=end_date+' '+end_time
        self.startdate=datetime.strptime(mod_start_date,"%d-%b-%Y %H:%M:%S")
        self.enddate=datetime.strptime(mod_end_date,"%d-%b-%Y %H:%M:%S")
        # Connects to database
        self.db=db_interface()

    def get_resultset(self):
        rtn=[]
        # Finds all the incidents that match the search criteria and return a list
        for result in self.db.collection.find( {"Incident_date": {"$gte": self.startdate, "$lt": self.enddate}}):
            rtn.append(result)
            #print (result)
        #print (rtn)
        return rtn
        
    def bar_resultset(self):
        reducer=Code("""
        function(obj, prev)
        {
            prev.count++;
        }
        """)
        
        result=self.db.collection.group(
                key={"Incident_type":1},
                condition={"Incident_date": {"$gte": self.startdate, "$lt": self.enddate}},
                initial={ "count" : 0 },
                reduce= reducer
            )
        return result
        #print (result)
    

#sample=QueryGenerator('21-Mar-2014', '24-Mar-2014', "05:06:07", "12:06:55")
#sample.get_resultset()
#sample.bar_resultset()
        
