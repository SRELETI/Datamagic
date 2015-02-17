Steps to run the Python project locally
---------------------------------------

### Step1:

Place the Crawler.py and Current_incident.py files in a folder and execute Current_incident.py. A file will be created
in “homedir/WRPS_DATA/PYTHON”. The file stores the crawled current incidents data from the Waterloo Police Department 
website.

### Step2:

Place the Sample_parser.py and Curr_parser.py in a folder and run the Curr_parser.py. This will parse the files 
which are crawled in the Step 1. The required data related to each incident is parsed and then inserted into 
MongoDB in JSON format. For inserting into the database, the database has to be setup first. 
Download and extract the latest MongoDB production release file. Then a data directory has to be setup. 
The default location of the data directory is C:\data\db. Then open the command prompt or terminal and navigate 
to MongoDB folder and run mongod.exe file. This will start the main MongoDB database process. 
A “waiting for connections” appears which indicate that the mongod.exe is running successfully. (These instructions
are for Windows only).

### Step3:

The Db.py file contains the connection information of the database. The parser creats an instance of the ``db_interface`` 
class in the DB.py file, then a connection to MongoDB is established and a database named “WRPS_DATA” is created 
if there is no database already with the same name. Then a collection (Table) with name ``WRPS_collection`` is 
created in the ``WRPS_DATA`` database. Finally, data is inserted into the ``WRPS_collection`` collection.

### Step4:

Run the Bottle_server.py file and open the URI http://localhost:8080/ in a webserver. Enter the start date, end date, 
start time and end time and click enter. This will submit the query to the query processor in the back end and the 
results will be displayed in the form of bar charts. Place all the files which are required from Step 1 to Step 4 in 
the same folder.
