import pymongo
import re
import logging

try:
    client=pymongo.MongoClient("mongodb://localhost:27017/")   
    mydatabase=client['phonedirectoryDb']     
    number_collection=mydatabase['numbers']

    phonelist=[]
    fetchlist=[] 

    # creating a .txt file to store contact details  

    class Directory:
    
        def details(self,name,address,mobileno,emailid):
            dict1={"name":name,"address":address,"mobileno":mobileno,"emailid":emailid}
            phonelist.append(dict1)

    obj=Directory()

    def validate(name,emailid):
        valname=re.search("[A-Za-z]{0,25}$",name)
        valemailid=re.search(r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b',emailid)
    
        if  valname and valemailid:
            return True
        else:
            return False    

    while(True):
        print("\n WELCOME TO THE PHONEBOOK DIRECTORY")
        print( "\nMAIN MENU")
        print("\n 1. Add a new Contact:")
        print("\n 2. Show all existing Contacts:")
        print("\n 3. Search the existing Contact using name:")
        print("\n 4. Search the existing contact using number:")
        print("\n 5. Delete the contact using number:")
        print("\n 6. Update the contact address and mobile number using name:")
        print("\n 7. Exit")
        choice = int(input("\n Enter your choice: "))
    
            
        #Adding contact

        if choice==1:
            name=input("\n Enter name:")
            emailid=input("\n Enter email id:")
        
            if validate(name,emailid):
                address=input("\n Enter address:")
                mobileno=int(input("\n Enter mobile number:"))
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
            sname=input("\n Enter name to search:")
            result=number_collection.find({"name":sname})
            for i in result:
                fetchlist.append(i)
            print(fetchlist) 

            #search for contact using number
            
        if choice==4:

            snumber=int(input("\n Enter number to search:"))
            result=number_collection.find({"mobileno":snumber})  
            for i in result:
                fetchlist.append(i)
            print(fetchlist)    

            #Deleting the contact

        if choice==5:

            del_contact=int(input("\n Enter the contact number to delete:"))
            result=number_collection.delete_one({"mobileno":del_contact})
            print(fetchlist) 

            #Updating the contact 

        if choice==6:

            updname=input("\n Enter the name whose contact details to update:")
            newaddress=input("\n Enter new address:")
            newmobileno=int(input("\n Enter new mobile number:"))
            result=number_collection.update_one({"name":updname},{"$set":{"address":newaddress,"mobileno":newmobileno}})
            print(fetchlist)  

        if choice==7:
            print("\n Thankyou for choosing phone directory!!")
            print("\n Exit from the menu:")
            break      

except:
    logging.error("Error occured")



