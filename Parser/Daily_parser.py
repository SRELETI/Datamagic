from Sample_parser import Parser

import re
from bs4 import BeautifulSoup
import json
import pprint

# Collects complete information related to Daily_call_summary
class Daily_call_summary(Parser):
    def __init__(self,preprocess_dir,processed_dir):
        super(Daily_call_summary,self).__init__(preprocess_dir,processed_dir)
        # Key
        self.incident_type="Incident_type"
        # Matches the incident type for each incident
        self.incident_type_re=r'<div class="incidenttype">(.*?)</div>'
        # Key
        self.incident_number="Incident_number"
        # Matches the incident number for each incident
        self.incident_number_re=r"Incident #: </strong>(.*?)</div>"
        # Key
        self.incident_date="Incident_date"
        # Matches the incident date for each incident
        self.incident_date_re=r"Incident Date: </strong>(.*?)</div>"
        # Key
        self.incident_location="Incident_location"
        # Matches the incident location for each incident
        self.incident_location_re=r"Location: </strong>(.*?)</div>"
        self.execute()

    def extract(self,line):
        rtn={} #empty list 
        self.type_matched=re.findall(self.incident_type_re,line,re.DOTALL)
        self.number_matched=re.findall(self.incident_number_re,line,re.DOTALL)
        self.date_matched=re.findall(self.incident_date_re,line,re.DOTALL)
        self.location_matched=re.findall(self.incident_location_re,line,re.DOTALL)
        # check for a match and then insert into the list
        if self.type_matched !=None:
            rtn[self.incident_type]=self.type_matched
        if self.date_matched !=None:
            rtn[self.incident_date]=self.date_matched
        if self.location_matched !=None:
            rtn[self.incident_location]=self.location_matched
        if self.number_matched !=None:
            rtn[self.incident_number]=self.number_matched
        return rtn # return list

    def parse(self,contents):
        rtn=[]
        # returns list containing information related to all incidents
        relevant_data=re.findall(r'<div class="incident">.*?</div>\s*</div>',contents,re.DOTALL)
        # If no incidents, then return
        if len(relevant_data)==0:
            return
        # Process each information in the list and store as key value pairs
        for index in range(0,len(relevant_data)):
            rtn.append((self.extract(relevant_data[index])))
        return rtn

                 	                
daily_call_parser=Daily_call_summary(r'C:\Users\sudeep\WRPS_DATA\PYTHON\daily_call_summary\preprocess',r'C:\Users\sudeep\WRPS_DATA\PYTHON\daily_call_summary\processed')
