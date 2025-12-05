from pymongo import MongoClient
from bson import ObjectId
import pprint

# -------------------------
# Database connection
# -------------------------
client = MongoClient("")  # adjust if using Atlas
db = client["university_db"]     
collection = db["students"]  

pp = pprint.PrettyPrinter(indent=2)#pretty printer for displaying documents in a readable format


# -------------------------
# CRUD Function Templates
# -------------------------

#function to insert a single document into the collection,this function gets the name and age from user and insert into the collection
def create_document():
    """Insert a single document into the collection."""
    name = input("Enter student name: ")#reads student name from user input  and converts it to a string
    age = int(input("Enter age: "))  #reads student age from user input and converts it to an integer
    student = {"name": name, "age": age} #creates a dictionary to store the student data,which is the name and age of the student
    res = collection.insert_one(student)#inserts the student data into the collection
    print(f"Document created: {student}")#prints confirmation message 

#function to insert a single document with a specific ID 
def create_document_with_id():
    """Insert a single document into the collection with a specific ID."""
    id = input("Enter student ID: ") #reads student id from user input  
    name = input("Enter student name: ")#reads student name from user input  
    age = int(input("Enter age: "))#reads student age from user input  
    student = {"_id": id, "name": name, "age": age} #creates a dictionary with given id  
    res = collection.insert_one(student)#inserts the document into the collection  
    print(f"Document created: {student}") #prints confirmation message  

#function to insert multiple documents  
def create_many_documents():
    """Insert multiple documents into the collection."""
    num = int(input("Enter number of documents to create: ")) #reads how many docs user wants to add  
    students = [] #list that will hold all student dictionaries  
    for i in range(num):  
        name = input("Enter student name: ") #reads student name from user input  
        age = int(input("Enter age: "))#reads student age from user input  
        student = {"name": name, "age": age}#creates the dictionary for one student  
        students.append(student) #adds dictionary to the list  
    res = collection.insert_many(students)#inserts all documents into the collection  
    print(f"Documents created: {students}") #prints confirmation message  

#function to fetch and print all documents  
def read_all_documents():
    """Fetch and print all documents."""
    docs = collection.find()#finds all documents in the collection  
    for doc in docs:  
        pp.pprint(doc)#pretty prints each document  

#function to fetch and print many documents by criteria
def read_many_documents():
    """Fetch and print many documents."""
    field = input("Enter field: ")#reads the field name from user input  
    value = input("Enter value: ") #reads the value from user input  
    docs = collection.find({field: value})#finds documents matching the field and value  
    for doc in docs:  
        pp.pprint(doc)#pretty prints each document  

#function to fetch and print the first document
def read_first_document():
    """Fetch and print the first document."""
    doc = collection.find_one()#finds the first document in the collection  
    pp.pprint(doc) #pretty prints the document 

#function to fetch and print a document by id
def read_document_by_id():
    """Fetch and print a document by ID."""
    id = input("Enter student ID: ")#reads the student id from user input  
    doc = collection.find_one({"_id": ObjectId(id)}) #finds the document with the given id  
    pp.pprint(doc) #pretty prints the document  

#function to fetch and print a document by criteria
def read_document_by_criteria():
    """Fetch and print a document by criteria."""
    field = input("Enter field: ")#reads the field name from user input  
    value = input("Enter value: ") #reads the value from user input  
    doc = collection.find_one({field: value}) #finds the document with the given field and value  
    pp.pprint(doc)#pretty prints the document  

#function to update a document by id 
def update_document_by_id():
    """Update a document by ID."""
    id = input("Enter student ID: ")#reads the student id from user input  
    field = input("Enter field: ")#reads the field name from user input  
    value = input("Enter value: ") #reads the value from user input  
    doc = collection.update_one({"_id": ObjectId(id)}, {"$set": {field: value}})#updates the document  
    pp.pprint(doc) #pretty prints the result  

#function to update many documents 
def update_many_documents():
    """Update many documents."""
    field = input("Enter field: ")#reads the field name from user input  
    value = input("Enter value: ") #reads the value from user input  
    doc = collection.update_many({field: value}, {"$set": {field: value}}) #updates all documents matching criteria  
    pp.pprint(doc)#pretty prints the result

#function to update a document
def update_document():
    """Update a document."""
    id = input("Enter student ID: ") #reads the student id from user input  
    field = input("Enter field: ")#reads the field name from user input  
    value = input("Enter value: ") #reads the value from user input  
    doc = collection.update_one({"_id": ObjectId(id)}, {"$set": {field: value}})#updates the document  
    pp.pprint(doc) #pretty prints the result

#function to delete a document by id 
def delete_document_by_id():
    """Delete a document by ID."""
    id = input("Enter student ID: ")#reads the student id from user input  
    doc = collection.delete_one({"_id": ObjectId(id)}) #deletes the document with the given id  
    pp.pprint(doc) #pretty prints the result

#function to delete a document by criteria 
def delete_document():
    """Delete a document."""
    id = input("Enter student ID: ")#reads the student id from user input  
    field = input("Enter field: ") #reads the field name from user input  
    value = input("Enter value: ")#reads the value from user input  
    doc = collection.delete_one({field: value}) #deletes the document matching criteria  
    pp.pprint(doc)#pretty prints the result

#function to delete all documents in the collect
def delete_all_documents():
    """Delete all documents."""
    doc = collection.delete_many({})#deletes all documents in the collection  
    pp.pprint(doc)#pretty prints the result

#function to delete many documents by criteria    
def delete_many_documents():
    """Delete many documents."""
    field = input("Enter field: ")#reads the field name from user input  
    value = input("Enter value: ") #reads the value from user input  
    doc = collection.delete_many({field: value})#deletes all documents matching criteria  
    pp.pprint(doc) #pretty prints the result
  



# -------------------------
# Menu System
# -------------------------

#menu system for selecting operations 
def menu():
    while True:
        #prints the menu header
        print()
        print("--- MongoDB Project Menu ---")
        print("1. Create Document")
        print("2. Create Document with ID")
        print("3. Create Many Documents")
        print("3. Read All Documents")
        print("4. Read Many Documents")
        print("5. Read First Document")
        print("6. Read Document by ID")
        print("7. Read Document by Criteria")
        print("8. Update Document by ID")
        print("9. Update Many Documents")
        print("10. Update Document")
        print("11. Delete Document by ID")
        print("12. Delete Document")
        print("13. Delete All Documents")
        print("14. Delete Many Documents")

        print("15. Exit")

        choice = input("Enter choice: ")#reads user's menu choice  

        #calls the functions according to what the user requseted
        if choice == "1":
            create_document()

        elif choice == "2":
            create_document_with_id()
        
        elif choice == "3":
            create_many_documents()

        elif choice == "3":
            read_all_documents()

        elif choice == "4":
            read_many_documents()

        elif choice == "5":
            read_first_document()

        elif choice == "6":
            read_document_by_id()

        elif choice == "7":
            read_document_by_criteria()

        elif choice == "8":
            update_document_by_id()
        

        elif choice == "10":
            update_document_by_id()

        elif choice == "11":
            delete_document_by_id()

        elif choice == "12":
            delete_document()

        elif choice == "13":
            delete_all_documents()

        elif choice == "14":
            delete_many_documents()

        elif choice == "15":
            print("Exiting...") #prints exit message  
            quit()#terminates program  
            break #breaks loop  

        else:
            print("Invalid choice, try again.") #prints error message if input invalid 

#runs the menu function when program starts 
if __name__ == "__main__":
    menu()
