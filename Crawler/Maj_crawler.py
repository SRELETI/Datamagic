#!/usr/bin/env python3.3

from Crawler import Crawler

class Maj_crawler(Crawler):
    def __init__(self,url,dir_suffix,crawl_interval):
        # Calling the parent class constructor
        super(Maj_crawler,self).__init__(url,dir_suffix,crawl_interval)
        self.execute()

''' Calling the Maj_crawler function
 The crawl interval is 16 hours''' 
maj_crawl=Maj_crawler('http://www.wrps.on.ca/major-incidents',
          'major_incidents',59600)
