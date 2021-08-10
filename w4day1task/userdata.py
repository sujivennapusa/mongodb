import pymongo
# 1.severname=localhost
# 2.database=StudentDb
# 3.username=
# 4.password=


studentlist=[]
client=pymongo.MongoClient("mongodb://localhost:27017/")   #establishing a connection
mydatabase=client['StudentDb']     #database
collection_name=mydatabase['students']   #collection


""" getName=input("enter the name:")
getRoll=input("enter the roll:")
getAdmno=input("enter the admno:")
getCollege=input("enter the college name:")
data={"name":getName,"rollno":getRoll,"admno":getAdmno,"college":getCollege}
print(data)

result=collection_name.insert_one(data)
print(result.inserted_id) """

""" result=collection_name.find({"rollno":"20"},{"_id":0})  # to print data without id and searching by rollno

for i in result:
   studentlist.append(i)
print(studentlist)   
"""
result=collection_name.find({"rollno":"20"})  # to print data  searching by rollno

for i in result:
   studentlist.append(i)
print(studentlist)   

