import pymongo
from datetime import datetime 
prodfetchlist=[]
receiver=pymongo.MongoClient("mongodb://localhost:27017/")   #establishing a connection
prodb=receiver['productDb']     #database
product_details=prodb["products"]   #collection
list=[]
class Product:
    def proDetails(self,name,productcode,distributor,manfyear,wholesaleprice,retailprice,description,mobileno):
        dict1={"name":name,"productcode":productcode,"distributor":distributor,"manfyear":manfyear,"wholesaleprice":wholesaleprice,"retailprice":retailprice,"description":description,"mobileno":mobileno}
        list.append(dict1)
obj=Product()
while(True):
    print("1.add products:")
    print("2.print api:")
    print("3.search products using product code:")
    choice=int(input("enter the choice:"))

    if choice==1:
        name=input("enter name:")
        productcode=int(input("enter product code:"))
        distributor=input("enter distributor name:")
        manfyear = str(input('Enter mfgdate(yyyy): '))
        wholesaleprice=int(input("enter wholesale price:"))
        retailprice=int(input("enter retail price:"))
        description=input("enter description: ")
        mobileno=int(input("enter mobileno:"))
        
        a=obj.proDetails(name,productcode,distributor,manfyear,wholesaleprice,retailprice,description,mobileno)
        result=product_details.insert_many(list)
                                                #prints the object ids
        print(result.inserted_ids)   

    if choice==2:
        result=product_details.find()    # prints tha data in the form of api
        for i in result:
            prodfetchlist.append(i)
        print(prodfetchlist)

    if choice==3:
        pcode=int(input("enter pcode:"))
        result=product_details.find({"productcode":pcode})    # prints tha data in the form of api
        for i in result:
            prodfetchlist.append(i)
        print(prodfetchlist)

    if choice==4:
        pcode=int(input("enter pcode to delete:"))
        result=product_details.delete_one({"productcode":pcode})    # delete the product of that particular code
        """ for i in result:
            prodfetchlist.append(i) """
        print(prodfetchlist)    


