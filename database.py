import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:8000/")

mydb = myclient["mydatabase"]

mycollection = mydb["customers"]


collist = mydb.list_collection_names()
if "customers" in  collist:
    print("the collection list exist.")

mydict = {"name": "Ezra Hampton",  "address": "100 grace hopper lane",}

x = mycollection.insert_one(mydict)