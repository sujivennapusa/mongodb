import pymongo
import re

client=pymongo.MongoClient("mongodb://localhost:27017/")   #establishing a connection
mydatabase=client['collegeDb']     #database
collection_name=mydatabase['students']
studentlist=[]

while(True):
    print("\n 1.Add students:")            
    print("\n 2.search students:")            
    print("\n 3.Update students:")            
    print("\n 4.Delete students:")            
    print("\n 5.to count the no of students from each branch:")
    print("\n 6.exit")
    choice=int(input("enter choice:"))
    if choice==1:
        name=input("enter name:")
        rollno=int(input("enter rollno:"))
        branch=input("enter branch:")
        mydict={"name":name,"rollno":rollno,"branch":branch} 
        
        studentlist.append(mydict)
        collection_name.insert_many(studentlist) 
        studentlist.clear()
        

    if choice==2:
        name=input("enter name to search:")
        result=collection_name.find({"name":name})
        for i in result:
            print(i)

    if choice==5:
        result=collection_name.aggregate([{"$group":{"_id":"$branch","no_of_students":{"$sum":1}}}])   
        for i in result:
            print(i)                           