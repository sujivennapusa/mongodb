import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017/")   #establishing a connection
mydatabase=client['StudentDb']     #database
collection_name=mydatabase['students']   #collection
result=collection_name.find_one() #find() is used to print all the data eith for loop

#find_one() is used to print the first data that we entered

print(result)
#for i in result:  #to print all the data
    #print(i)