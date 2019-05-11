import pymongo
import os

MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "myTestDB"
COLLECTION_NAME = "myFirstMDB"

#Mongo connect function
def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e

conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

"""
Insert 1 record

new_doc = {'first': 'douglas', 'last': 'adams', 'dob': '28/04/1948', 'gender': 'm', 'hair_colour': 'not much', 'occupation': 'writer', 'nationality': 'english'}
coll.insert(new_doc)
"""

"""
Insert many records

new_docs = [{'first': 'terry', 'last': 'pratchett', 'dob': '11/03/1952', 'gender': 'm', 'hair_colour': 'grey', 'occupation': 'writer', 'nationality': 'english'}, {'first': 'george', 'last': 'rr martin', 'dob': '20/09/1948', 'gender': 'm', 'hair_colour': 'white', 'occupation': 'writer', 'nationality': 'american'}]

coll.insert_many(new_docs)
"""

"""
Find specific data
documents = coll.find({'first': 'douglas'}) 

Remove data
coll.remove({'first': 'douglas'}) 

"""
coll.update_many({'nationality': 'american'}, {'$set':{'hair_colour': 'maroon'}}) 

documents = coll.find({'nationality': 'american'}) # call everything that's in the database.  this returns a MongoDB object



for doc in documents:
    print(doc)