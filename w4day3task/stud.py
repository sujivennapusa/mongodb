import pymongo

client=pymongo.MongoClient("mongodb://localhost:27017")
mydatabase=client['CollegeDb']    #database
collection_name=mydatabase['students'] 
studentlist=[]

fetchlist=[]

while(True):
    print("1.Add student:")
    print("2.search name:")
    print("3.Update student:")
    print("4.Delete Student:")
    print("5.view braches using count:")
    print("6.veiw all students:")
    print("7.exit")
    choice=int(input("enter your choice:"))

    if choice==1:
        name=input("enter your name:")
        roll=int(input("enter your roll:"))
        branch=input("enter branch:")
        mydict={"name":name,"roll":roll,"branch":branch,"del_falg":0}
        studentlist.append(mydict)
        collection_name.insert_many(studentlist)
        studentlist.clear()

    if choice==2:
        name=input("enter name:")
        result=collection_name.find({"name":name})
        for i in result:
            print(i)
   
    if choice==4:
        roll=int(input("enter the rollno to be deleted"))
        collection_name.update_one({"roll":roll},{"$set":{"del_flag":1}})

    if choice==5:
        result=collection_name.aggregate([{"$group": {"_id":"$branch","no_of_students":{"$sum":1}}}])
        for i in result:
            print(i)

    


    if choice==6:
         result=collection_name.find()
         for i in result:
          print(i)

    if choice==7:
        break