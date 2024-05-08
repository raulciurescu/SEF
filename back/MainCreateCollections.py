from pymongo import MongoClient
# make the code see the CreateTheDataBase file
import sys
sys.path.append('d:\\FULL_SEF_APP\\Back\\DataBase\\CreateCollections')
from DataBase.CreateCollections.CreateTheDataBase import create_database

# Create the connection to the MongoDB
client = MongoClient('localhost', 27017)

# Create the database
DB = client['FullAppSef']

# Create the collections
create_database(DB)
