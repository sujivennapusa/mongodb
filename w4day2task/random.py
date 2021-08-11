import pymongo
import re
import logging

client=pymongo.MongoClient("mongodb://localhost:27017/")   
mydatabase=client['phonedirectoryDb']     
number_collection=mydatabase['numbers']

phonelist=[]
fetchlist=[] 


    # creating a .txt file to store contact details  


try:
    class Directory:
        def init(self,name,address,mobileno,emailid):
            self.name=name
            self.address=address
            self.mobileno=mobileno
            self.emailid=emailid
        def details(self,name,address,mobileno,emailid):
            dict1={"name":name,"address":address,"mobileno":mobileno,"emailid":emailid}
            phonelist.append(dict1)

    def validate(emailid,mobileno):
        valemailid=re.search(r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b',emailid)
        valnum=re.search(r'^\+91-?\d{4}-?\d{3}-?\d{3}$|^0?\d{4}-?\d{3}-?\d{3}$',mobileno)
        if valemailid and valnum:
            return True
        else:
            return False    


    obj=Directory()

    


    while(True):
        print("WELCOME TO THE PHONEBOOK DIRECTORY")
        print( "\nMAIN MENU\n")
        print( "1. Add a new Contact:")
        print( "2. Show all existing Contacts:")
        print( "3. Search the existing Contact using name:")
        print( "4. Exit")
        choice = int(input("Enter your choice: "))
    
            
        #Adding contact
        if choice==1:

            print("ADD NEW CONTACT")
            name=input("Enter name:")
            address=input("Enter address:")
            mobileno=int(input("Enter mobile number:"))
            emailid=input("Enter email id:")

            if validate(emailid,mobileno)==True:
                contactDetails=obj.details(name,address,mobileno,emailid)
                result=number_collection.insert_many(phonelist)
                print(result.inserted_ids) 
            
            # prints tha data in the form of api

        if choice==2:

            result=number_collection.find()
            for i in result:
                fetchlist.append(i)
            print(fetchlist)
        
            # searching for contact using name

        if choice==3:

            sname=input("enter name to search:")
            result=number_collection.find({"name":sname})
            for i in result:
                fetchlist.append(i)
            print(fetchlist) 

            #search for contact using number
            
        if choice==4:

            snumber=int(input("enter number to search:"))
            result=number_collection.find({"mobileno":snumber})  
            for i in result:
                fetchlist.append(i)
            print(fetchlist)    

            #Deleting the contact

        if choice==5:

            del_contact=int(input("Enter the contact number to delete:"))
            result=number_collection.delete_one({"mobileno":del_contact})
            print(fetchlist) 

            #Updating the contact 

        if choice==6:

            updname=input("Enter the name whose contact details to update:")
            newaddress=input("Enter new address:")
            newmobileno=int(input("Enter new mobile number:"))
            result=number_collection.update_one({"name":updname},{"$set":{"address":newaddress,"mobileno":newmobileno}})
            print(fetchlist)  

        if choice==7:
            print("Exit from the menu:")
            break      


except:
    logging.error("Error occured")
