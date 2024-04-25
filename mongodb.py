import pymongo
import sys


def updateData(mydict):
    
    try:
        client = pymongo.MongoClient("Your Mongodb link here")
        print("Connected successfully!!!")
    except pymongo.errors.ConfigurationError:
        print("An Invalid URI host error was received. Is your Atlas host name correct in your connection string?")
        sys.exit(1)
    
    mydb = client["ParkEase"]
    mycol = mydb["ParkingSpaces"]
    # Find the document using its _id
    existing_document = mycol.distinct("_id")
    if existing_document[0]:
        # Update the existing document
        result = mycol.update_one({"_id": existing_document[0]}, {"$set": mydict})
        print("Document updated.")
    else:
        insert_result = mycol.insert_one(mydict)
        print("Document inserted.")


    
# def getData():
#     existing_document = mycol.distinct("_id")

#     if existing_document[0]:
#         # getting the existing document
#         inserted_data = mycol.find_one({"_id": existing_document[0]})
#         print(inserted_data)
#     else:
#         all_documents = mycol.find()
#         for document in all_documents:
#             print(document)
            
# mydb = client["ParkEase"]
# mycol = mydb["ParkingSpaces"]
# mydict = {"FreeSpacesLocation": "1,2,3,4,5,6", "TotalSpaces": "11", "Occupied": "3", "FreeSpaces": "8"}
# updateData(mydict)
# #getData()

