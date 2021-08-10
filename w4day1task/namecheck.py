import pymongo

studentlist=[]
client=pymongo.MongoClient("mongodb://localhost:27017/")   #establishing a connection
mydatabase=client['StudentDb']     #database
collection_name=mydatabase['students']   #collection
result=collection_name.find({"name":{"$regex":"[^r]"}},{"_id":0})  # to print the name which start with 'r'
#result=collection_name.find({"name":{"$regex":"[v$]"}},{"_id":0})  # to print the name which end with 'v'
#result=collection_name.find({"name":{"$regex":"[^s]i$"}},{"_id":0})  #to print name which start with 's' and end with 'i'

for i in result:
   studentlist.append(i)
print(studentlist)   