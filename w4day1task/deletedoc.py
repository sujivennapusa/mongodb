import pymongo

studentlist=[]
client=pymongo.MongoClient("mongodb://localhost:27017/")   #establishing a connection
mydatabase=client['StudentDb']     #database
collection_name=mydatabase['students']   #collection
result=collection_name.delete_one({"name":"suji"})  # to delete data using key and value of one document

result=collection_name.delete_many({"name":"suji"})  # to delete data using key and value of many documents

result=collection_name.delete_one({"name":{"$regex":"^n"}})  # using regex deleting name which start with 'n'

result=collection_name.delete_many({}) # delete all data 

# when we use delete function we should not use for loop

# when we use delete_one function to delete the name which is repeated,then it will delete the last one 

print(studentlist)   

print(result.deleted_count)
