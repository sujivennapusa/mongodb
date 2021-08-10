import pymongo
fetchlist=[]
client=pymongo.MongoClient("mongodb://localhost:27017/")   #establishing a connection
mydb=client['employeeDb']     #database
employees=mydb["employees"]   #collection
list=[]
class Employee:
    def empdetails(self,name,address,mobileno,designation,salary,companyname):
        dict1={"name":name,"address":address,"mobileno":mobileno,"designation":designation,"salary":salary,"companyname":companyname}
        list.append(dict1)
obj=Employee()
while(True):
    print("1.add employee:")
    print("2.print api:")
    choice=int(input("enter the choice:"))

    if choice==1:
        name=input("enter name:")
        address=input("enter address:")
        mobileno=int(input("enter mobileno:"))
        designation=input("enter designation:")
        salary=int(input("enter salary:"))
        companyname=input("enter companyname:")
        a=obj.empdetails(name,address,mobileno,designation,salary,companyname)
        result=employees.insert_many(list)
                                                #prints the object ids
        print(result.inserted_ids)   

    if choice==2:
        result=employees.find()    # prints tha data in the form of api
        for i in result:
            fetchlist.append(i)
        print(fetchlist)  

        
        


    if choice==3:
        result=employees.find_one()  # prints only first data using find_one()
        print(result)
        
    if choice==4:
        result=employees.find()            #prints all the data using find()
        for i in result:
            print(i)

    if choice==5:
        #result=employees.find({},{"_id":0})   # To avoid id using find({},{"_id":0}) 

        result=employees.find({},{"_id":0,"name":0})   # To avoid id  and name using find({},{"_id":0,"name":0}) 
        for i in result:
            fetchlist.append(i) 
        print(fetchlist)        

    if choice==6:
        result=employees.find({},{"_id":0,"name":1})   # To print name only using find({},{"name":1}) 
        for i in result:
           fetchlist.append(i) 
        print(fetchlist)   

    if choice==7:
            
             #to search an employee using name


        result=employees.find({"name":"nani"})  
        for i in result:
            fetchlist.append(i)
        print(fetchlist)           

    if choice==8:
            
             #to search an employee using name


        result=employees.delete_many({"name":"nani"})  
        """ for i in result:
            fetchlist.append(i) """
        print(fetchlist)           
