#!/usr/bin/env python3.3
from Crawler import Crawler

class Current_incident(Crawler):
    def __init__(self,url,dir_suffix,crawl_interval):
        # calling the constructor of the parent class
        super(Current_incident,self).__init__(url,dir_suffix,crawl_interval)
        self.execute()

''' calling the current_incident function
  The Crawl_interval is 596 seconds for current incidents'''
cur_crawler=Current_incident('http://www.wrps.on.ca/current-incidents','current_incident',596)

