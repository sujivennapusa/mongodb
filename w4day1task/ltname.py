import pymongo

studentlist=[]
client=pymongo.MongoClient("mongodb://localhost:27017/")   #establishing a connection
mydatabase=client['StudentDb']     #database
collection_name=mydatabase['students']   #collection
#result=collection_name.find({"name":{"$lt":"r"}},{"_id":0})  # to print the name which is lessthan than  'r'
result=collection_name.find({"rollno":{"$lt":"26"}},{"_id":0})  # to print the rollno which is less than  '26'


for i in result:
   studentlist.append(i)
print(studentlist)   