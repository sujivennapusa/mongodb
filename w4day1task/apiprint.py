import pymongo
# 1.severname=localhost
# 2.database=StudentDb
# 3.username=
# 4.password=


studentlist=[]
client=pymongo.MongoClient("mongodb://localhost:27017/")   #establishing a connection
mydatabase=client['StudentDb']     #database
collection_name=mydatabase['students']   #collection
result=collection_name.find()
for i in result:
    studentlist.append(i)
print(studentlist)
