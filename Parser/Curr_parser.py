from Sample_parser import Parser

import re
from bs4 import BeautifulSoup
import json
import pprint
from datetime import datetime

# Collect complete information related to current incidents 
class Current_incident(Parser):
    def __init__(self,preprocess_dir,processed_dir):
        super(Current_incident,self).__init__(preprocess_dir,processed_dir)
        # key 
        self.incident_type="Incident_type"
        # Matches the incident type for each incident
        self.incident_type_re=r'<div class="incidenttype">(.*?)</div>'
        # key
        self.incident_number="Incident_number"
        # Matches the incident number for each incident
        self.incident_number_re=r"Incident #: </strong>(.*?)</div>"
        # key
        self.incident_date="Incident_date"
        # Matches the incident date for each incident
        self.incident_date_re=r"Incident Date: </strong>(.*?)</div>"
        # key
        self.incident_location="Incident_location"
        # Matches the incident location for each incident
        self.incident_location_re=r"Location: </strong>(.*?)</div>"
        # key
        self.incident_map="Incident_map"
        # Gets the map info for the incident
        self.incident_map_re="https\:\/\/maps\.google\.ca\/maps\?q\=(.*?)\,\+(.*?)\""
        self.execute()

    def extract(self,line):
        rtn={} #empty list
        self.type_matched=re.findall(self.incident_type_re,line,re.DOTALL)
        self.number_matched=re.findall(self.incident_number_re,line,re.DOTALL)
        self.date_matched=re.findall(self.incident_date_re,line,re.DOTALL)
        self.location_matched=re.findall(self.incident_location_re,line,re.DOTALL)
        self.map_matched=re.findall(self.incident_map_re,line)
        # Check if there is a match and if so, then insert into the list with the corresponding key
        if len(self.map_matched) >0:
            self.map_matched_mod=[float(i) for i in self.map_matched[0]]
            rtn[self.incident_map]=self.map_matched_mod
        if len(self.type_matched)>0:
            rtn[self.incident_type]=self.type_matched[0]
        if len(self.date_matched) >0:
            rtn[self.incident_date]=datetime.strptime(self.date_matched[0],"%b %d, %Y %H:%M:%S %p")
        if len(self.location_matched)>0:
            rtn[self.incident_location]=self.location_matched[0]
        if len(self.number_matched) >0:
            rtn[self.incident_number]=self.number_matched[0]
        return rtn # return list


    def parse(self,contents):
        rtn=[]
        # Gives a list containing information related to all incidents
        relevant_data=re.findall(r'<div class="incident">.*?</div>\s*</div>',contents,re.DOTALL)
        # If no incidents, then return
        if len(relevant_data)==0:
            return
        # Process each information in the list and store as key value pairs
        for index in range(0,len(relevant_data)):
                rtn.append(self.extract(relevant_data[index]))
        return rtn
       


sample_parser=Current_incident(r'C:\Users\sudeep\WRPS_DATA\PYTHON\current_incident\preprocess',r'C:\Users\sudeep\WRPS_DATA\PYTHON\current_incident\processed')
