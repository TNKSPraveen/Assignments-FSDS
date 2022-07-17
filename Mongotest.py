import pymongo

client = pymongo.MongoClient("mongodb+srv://tnksp:Mech1234@cluster0.m74m9.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d = {
    "name" : "sudhanshu123",
    "email": "sudhanshu@ineuron.ai",
    "surname" : "kumar"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)
