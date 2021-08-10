import pymongo

studentlist=[]
client=pymongo.MongoClient("mongodb://localhost:27017/")   #establishing a connection
mydatabase=client['StudentDb']     #database
collection_name=mydatabase['students']   #collection
result=collection_name.find({"name":{"$gt":"b"}},{"_id":0})  # to print the name which is greater than or equal to 'b'
result=collection_name.find({"name":{"$gt":"y"}},{"_id":0})  # to print the name which is greater than or equal to 'y'
result=collection_name.find({"name":{"$gt":"s"}},{"_id":0})  # to print the name which is greater than or equal to 's'
result=collection_name.find({"rollno":{"$gt":"26"}},{"_id":0})  # to print the rollno which is greater than or equal to '26'


for i in result:
   studentlist.append(i)
print(studentlist)   