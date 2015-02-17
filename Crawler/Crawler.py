#!/usr/bin/env python3.3

import os
import time
import datetime
import urllib.request
class Crawler:
    'Crawler class:'
    # os.path.expanduser() returns the user's home directory
    homedir=os.path.expanduser('~')
    # The os.path.join() function constructs a pathname out of one or more partial pathnames.
    base_dir=os.path.join(homedir,"WRPS_DATA","PYTHON")
    # Constructor for the class
    def __init__(self,url,dir_suffix,crawl_interval):
        self.url=url
        self.dir_suffix=dir_suffix
        self.crawl_interval=crawl_interval
        self.preprocess_dir=os.path.join(Crawler.base_dir,dir_suffix,"preprocess")
        self.processed_dir=os.path.join(Crawler.base_dir,dir_suffix,"processed")

    def execute(self):
        try:
            # creates directory 
            os.makedirs(self.preprocess_dir)
            os.makedirs(self.processed_dir)
        except OSError:
            # skip if already created
            pass
        while(1):
            # returns the current time 
            cur_min=datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            # sends a request to open the url and saves the response
            response=urllib.request.urlopen(self.url)
            file_name=cur_min+'.txt'
            path=os.path.join(self.preprocess_dir,file_name)
            # creating a file in the particular path if the file doesn't exist already
            outfile=open(path,'wb')
            # Writes to the file
            outfile.write(response.read())
            # Close the file
            outfile.close()
            # Sleep for particular time before starting the next crawl
            time.sleep(self.crawl_interval)


            
        
                          
