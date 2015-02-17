#!/usr/bin/env python3.3

from Crawler import Crawler

class Daily_summary(Crawler):
    def __init__(self,url,dir_suffix,crawler_interval):
        #Calling the parent class constructor
        super(Daily_summary,self).__init__(url,dir_suffix,crawler_interval)
        self.execute()

# Calling the parent class constructor
# The crawl_interval for daily_summary is 12 hours
maj_crawler=Daily_summary('http://www.wrps.on.ca/daily-call-summary','daily_call_summary',43200)
