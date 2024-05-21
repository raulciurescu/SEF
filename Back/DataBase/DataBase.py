from pymongo import MongoClient
from Create.Create import create_database

# Create the connection to the MongoDB
client = MongoClient('localhost', 27017)

# Create the database
DB = client['FullAppSef']



# Create the collections
create_database(DB)
