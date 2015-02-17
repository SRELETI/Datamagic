from Sample_parser import Parser

import re
from bs4 import BeautifulSoup
import json

# Collect complete information related to Major incidents
class Major_incident(Parser):
    def __init__(self,preprocess_dir,processed_dir):
        super(Major_incident,self).__init__(preprocess_dir,processed_dir)
        # key 
        self.incident_type="Incident_type"
        # Matches the incident type for each incident
        self.incident_type_re=r'<div class="incidenttype">(.*?)</div>'
        # key
        self.incident_number="Incident_number"
        # Matches the incident number for each incident
        self.incident_number_re=r"Incident #: </strong>(.*?)</div>"
        # Key
        self.incident_publish_date="Incident Publish Date"
        # Matches the incident publish date for each incident
        self.incident_publish_date_re=r"Publish Date: </strong>(.*?)</div>"
        # key
        self.incident_date="Incident_date"
        # Matches the incident date for each incident
        self.incident_date_re=r"Incident Date: </strong>(.*?)</div>"
        # key
        self.incident_location="Incident_location"
        # Matches the incident location for each incident
        self.incident_location_re=r"Location: </strong>(.*?)</div>"
        # Key
        self.incident_summary="Incident_summary"
        # Matches the incident summary for each incident
        self.incident_summary_re=r"<p>(.*?)</p>"
        self.execute()

    def extract(self,line):
        rtn={} #empty list
        self.type_matched=re.findall(self.incident_type_re,line)
        self.number_matched=re.findall(self.incident_number_re,line)
        self.publish_matched=re.findall(self.incident_publish_date_re,line)
        self.date_matched=re.findall(self.incident_date_re,line)
        self.location_matched=re.findall(self.incident_location_re,line)
        self.summary_matched=re.findall(self.incident_summary_re,line)
        # Check if there is a match and if so, then insert into the list with the corresponding key
        if self.type_matched !=None:
            rtn[self.incident_type]=self.type_matched
        if self.date_matched !=None:
            rtn[self.incident_date]=self.date_matched
        if self.publish_matched !=None:
            rtn[self.incident_publish_date]=self.publish_matched
        if self.location_matched !=None:
            rtn[self.incident_location]=self.location_matched
        if self.number_matched !=None:
            rtn[self.incident_number]=self.number_matched
        if self.summary_matched !=None:
            rtn[self.incident_summary]=self.summary_matched
        return rtn # return list

    def parse(self,contents):
        rtn=[]
        # Gives a list containing information related to all incidents
        relevant_data=re.findall(r'<div class="incident ">.*?</div>\s*</div>',contents,re.DOTALL)
        # If no incidents, then return
        if len(relevant_data)==0:
            return
        # Process each information in the list and store as key value pairs
        for index in range(0,len(relevant_data)):
            rtn.append(self.extract(relevant_data[index]))
        return json.dumps(rtn)


major_parser=Major_incident(r'C:\Users\sudeep\WRPS_DATA\PYTHON\major_incidents\preprocess',r'C:\Users\sudeep\WRPS_DATA\PYTHON\major_incidents\processed')

