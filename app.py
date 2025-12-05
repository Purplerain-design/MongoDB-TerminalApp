from pymongo import MongoClient
from bson import ObjectId
import pprint

# -------------------------
# Database connection
# -------------------------
client = MongoClient(
    "mongodb+srv://g24m4379_db_user:3Aq81i7mISjgTwNh@cspracproject.ypxyrm5.mongodb.net/?retryWrites=true&w=majority&appName=CSPracProject"
)  # adjust if using Atlas
db = client["university_db"]  # replace with your chosen DB name
collection = db["students"]  # example collection
# use pretty print to display docs in a readable format
pp = pprint.PrettyPrinter(indent=2)


# -------------------------
# CRUD Functions
# -------------------------


def create_document():
    """Insert a single document into the collection."""
    # take user input, convrt into int for an age
    name = input("Enter student name: ")
    age = int(input("Enter age: "))
    student = {
        "name": name,
        "age": age,
    }
    # create a dictionary to store the student data,which is the name and age of the student
    # insert the student data into the collection and,
    # print confirmation message
    res = collection.insert_one(student)
    print(f"Document created: {student}")


def create_document_with_id():
    """Insert a single document into the collection with a specific ID."""
    # take user input for id, name, etc
    id = input("Enter student ID: ")
    name = input("Enter student name: ")
    age = int(input("Enter age: "))
    student = {
        "_id": id,
        "name": name,
        "age": age,
    }
    # create a dictionary with given id and insert the document into the collection
    # print confirmation message
    res = collection.insert_one(student)
    print(f"Document created: {student}")


def create_many_documents():
    """Insert multiple documents into the collection."""
    # read how many docs user wants to add
    num = int(input("Enter number of documents to create: "))
    # stores all student dictionaries
    students = []

    # take user input for name,age, and create a dictionary for one student
    # and append dictionary to the list
    for i in range(num):
        name = input("Enter student name: ")
        age = int(input("Enter age: "))
        student = {"name": name, "age": age}
        students.append(student)

    # inserts all documents into the collection and,
    # # prints confirmation message
    res = collection.insert_many(students)
    print(f"Documents created: {students}")


def read_all_documents():
    """Fetch and print all documents."""

    # find all documents in the collection and
    # print each document
    docs = collection.find()
    for doc in docs:
        pp.pprint(doc)


def read_many_documents():
    """Fetch and print many documents."""
    # read the field name and value from user input
    field = input("Enter field: ")
    value = input("Enter value: ")
    docs = collection.find({field: value})
    # find documents matching the field and value
    # print each document
    for doc in docs:
        pp.pprint(doc)


def read_first_document():
    """Fetch and print the first document."""
    # finds the first document in the collection and,
    # print the document
    doc = collection.find_one()
    pp.pprint(doc)


def read_document_by_id():
    """Fetch and print a document by ID."""
    # read the student id from user input and find the doc with the given id
    # print the document
    id = input("Enter student ID: ")
    doc = collection.find_one({"_id": ObjectId(id)})
    pp.pprint(doc)


def read_document_by_criteria():
    """Fetch and print a document by criteria."""
    # read the field name and value from user input,
    # find the document with the given field and value
    # print the document
    field = input("Enter field: ")
    value = input("Enter value: ")
    doc = collection.find_one({field: value})
    pp.pprint(doc)


def update_document_by_id():
    """Update a document by ID."""
    # take user input for the id, filed and value,update the document, and
    # print results
    id = input("Enter student ID: ")
    field = input("Enter field: ")
    value = input("Enter value: ")
    doc = collection.update_one({"_id": ObjectId(id)}, {"$set": {field: value}})
    pp.pprint(doc)


def update_many_documents():
    """Update many documents."""
    # take user input for field name and value
    # update all docs by matching criteria and print results
    field = input("Enter field: ")
    value = input("Enter value: ")
    doc = collection.update_many({field: value}, {"$set": {field: value}})
    pp.pprint(doc)


def update_document():
    """Update a document."""
    # take user input for id, field name and value
    # update the document and print results
    id = input("Enter student ID: ")
    field = input("Enter field: ")
    value = input("Enter value: ")
    doc = collection.update_one({"_id": ObjectId(id)}, {"$set": {field: value}})
    pp.pprint(doc)


def delete_document_by_id():
    """Delete a document by ID."""
    # read the student id from user input
    # delete the doc with the given id and print results
    id = input("Enter student ID: ")
    doc = collection.delete_one({"_id": ObjectId(id)})
    pp.pprint(doc)


def delete_document():
    """Delete a document by criteria."""
    # take user input for id, field name and value
    # delete the document matching criteria and print results
    id = input("Enter student ID: ")
    field = input("Enter field: ")
    value = input("Enter value: ")
    doc = collection.delete_one({field: value})
    pp.pprint(doc)


def delete_all_documents():
    """Delete all documents."""
    # delete all documents in the collection and print results
    doc = collection.delete_many({})
    pp.pprint(doc)


def delete_many_documents():
    """Delete many documents."""
    # reads the field name and value from user input
    # deletes all documents matching criteria
    field = input("Enter field: ")
    value = input("Enter value: ")
    doc = collection.delete_many({field: value})
    pp.pprint(doc)


# -------------------------
# Advanced  Querying
# -------------------------


def and_function(collection):
    """uses AND operator"""
    # stores conditions entered by the user
    conditions_list = []
    # take input from yhe user(no of conditions)
    # and convert it into int

    no_of_conditions = input("Enter a number of conditions: ")
    num = int(no_of_conditions)

    for i in range(num):
        field = input("Enter field: ")
        value = input("Enter value: ")

        #  store them as a dictionary to the list
        conditions_list.append({field: value})

    # perfom a query using $and operator and return the doc that matches
    # if docs were found, print each matching doc
    students = list(collection.find({"$and": conditions_list}))
    if len(students) > 0:
        for student in students:
            print("Student Found! ")
            print(student)
    else:
        print("student not found")


def or_function(collection):
    """uses OR operator"""
    # stores conditions entered by the user
    conditions_list = []

    # take input from yhe user(no of conditions)
    # and convert it into int
    no_of_conditions = input("Enter a number of conditions: ")
    num = int(no_of_conditions)

    for i in range(num):
        field = input("Enter field: ")
        value = input("Enter value: ")

        #  store them as a dictionary to a list
        conditions_list.append({field: value})

    # perfom a query using $or operator and return the doc that matches
    # if docs were found, print each matching doc
    students = list(collection.find({"$or": conditions_list}))
    if len(students) > 0:
        for student in students:
            print("Student Found! ")
            pp.pprint(student)
    else:
        print("student not found")


def not_function(collection):
    """uses NOT operator"""
    # stores conditions entered by the user
    conditions_list = []

    field = input("Enter field: ")
    value = input("Enter value: ")

    #  store them as a dictionary to a list
    conditions_list.append({field: value})

    # perfom a query using $not operator and return the doc that matches
    # if docs were found, print each matching doc
    students = list(collection.find({field: {"$not": {"$eq": value}}}))
    if len(students) > 0:
        for student in students:
            print("Student Found! ")
            pp.pprint(student)
    else:
        print("student not found")


def comparison_operators(collection):
    """uses comparison operators"""

    # ask the user the comparison they want to use
    operator = input("Choose operator you want to use? ( $gt, $lt, $in,$exists): ")

    # -------------------------
    # handles $gt operator
    # -------------------------

    if operator == "$gt":

        field = input("Enter field: ")
        value = int(input("Enter numeric value: "))

        # find all docs where field value is greater than
        # value given by the user, if those docs were found print them
        students = list(collection.find({field: {"$gt": value}}))
        if len(students) > 0:
            for student in students:
                print("Student Found! ")
                pp.pprint(student)
        else:
            print("student not found")

    # -------------------------
    # handles $lt operator
    # -------------------------

    if operator == "$lt":

        field = input("Enter field: ")
        value = int(input("Enter numeric value: "))

        # find all docs where field value is less than
        # value given by the user, if those docs were found print them
        students = list(collection.find({field: {"$lt": value}}))
        if len(students) > 0:
            for student in students:
                print("Student Found! ")
                pp.pprint(student)
        else:
            print("student not found")

    # -------------------------
    # handles the $in operator
    # -------------------------

    if operator == "$in":

        # stores the values to be checked
        values_list = []
        field = input("Enter field: ")

        no_of_values = int(input("Enter number of values: "))

        # collect multiple values from the user and append them to a list
        for i in range(no_of_values):
            value = int(input("Enter value: "))
            values_list.append(value)

        # find all docs where field value matches any value in a list
        # value given by the user, if those docs were found print them
        students = list(collection.find({field: {"$in": values_list}}))
        if len(students) > 0:
            for student in students:
                print("Student Found! ")
                pp.pprint(student)
        else:
            print("student not found")

    # -------------------------
    # handles the $exists operator
    # -------------------------

    if operator == "$exists":
        field = input("Enter field name: ")

        # find all docs that contain the given field
        # if those docs were found print them
        students = list(collection.find({field: {"$exists": True}}))
        if len(students) > 0:
            for student in students:
                print("Student Found! ")
                pp.pprint(student)
        else:
            print("student not found")


# -------------------------
# Agregation pipelines
# -------------------------


def match_documents():
    """Match documents"""
    print("----Matching documents----")
    print("1. Find the total number of courses completed per student.")
    print("2. Find the total number of students per course.")

    # prompt user for input to choose aggregation
    choice = input("Enter choice: ")

    match choice:
        case "1":
            # Define aggregation pipelines
            # unwind,match, group,project,and sort data for courses per student
            # and count completed courses per student
            match = [
                {"$unwind": "$enrolled_courses"},
                {"$match": {"enrolled_courses.status": "Completed"}},
                {"$group": {"_id": "$name", "count": {"$sum": 1}}},
                {
                    "$project": {
                        "Student": "$_id",
                        "Completed Courses": "$count",
                        "_id": 0,
                    }
                },
                {"$sort": {"Total Students": -1}},
            ]
            # execute aggregation and print results
            docs = collection.aggregate(match)
            print("\nTotal number of Students per depatment")
            for doc in docs:
                pp.pprint(doc)

        case "2":
            # define aggregation pipeline
            # unwind,match, group,project and sort data for students per courses
            # and count student per course
            match = [
                {"$unwind": "$enrolled_courses"},
                {
                    "$group": {
                        "_id": "$enrolled_courses.course_code",
                        "total_students": {"$addToSet": "$student_id"},
                    }
                },
                {
                    "$project": {
                        "Course Code": "$_id",
                        "Total Students": {"$size": "$total_students"},
                        "_id": 0,
                    }
                },
                {"$sort": {"Total Students": -1}},
            ]
            # execute aggregation and print results
            docs = collection.aggregate(match)
            print("\nTotal number of Students per courses")
            for doc in docs:
                pp.pprint(doc)
# -------------------------
# Aggregation with $lookup and $merge
# -------------------------


def lookup_aggregation():
    """Aggregation using $lookup to join students and courses."""
    print("----Aggregation using $lookup----")

    # perform a join between 'students' and 'courses' collections
    # unwind enrolled_courses and lookup corresponding course info
    pipeline = [
        {"$unwind": "$enrolled_courses"},
        {
            "$lookup": {
                "from": "courses",  # collection to join
                "localField": "enrolled_courses.course_code",  # field in students
                "foreignField": "course_code",  # field in courses
                "as": "course_details",  # output array field
            }
        },
        {"$unwind": "$course_details"},
        {
            "$project": {
                "_id": 0,
                "Student Name": "$name",
                "Student ID": "$student_id",
                "Course Code": "$enrolled_courses.course_code",
                "Course Name": "$course_details.course_name",
                "Department": "$course_details.department",
                "Status": "$enrolled_courses.status",
                "Grade": "$enrolled_courses.grade",
            }
        },
    ]

    # execute the aggregation pipeline and print results
    docs = collection.aggregate(pipeline)
    print("\nJoined Student-Course Details:")
    for doc in docs:
        pp.pprint(doc)


def lookup_and_merge_aggregation():
    """Aggregation using $lookup and $merge to create a summary collection."""
    print("----Aggregation using $lookup and $merge----")

    # join students with courses and merge summarized results
    pipeline = [
        {"$unwind": "$enrolled_courses"},
        {
            "$lookup": {
                "from": "courses",
                "localField": "enrolled_courses.course_code",
                "foreignField": "course_code",
                "as": "course_info",
            }
        },
        {"$unwind": "$course_info"},
        {
            "$group": {
                "_id": "$student_id",
                "Student Name": {"$first": "$name"},
                "Total Courses": {"$sum": 1},
                "Departments": {"$addToSet": "$course_info.department"},
            }
        },
        {
            "$project": {
                "_id": 0,
                "Student ID": "$_id",
                "Student Name": 1,
                "Total Courses": 1,
                "Departments": 1,
            }
        },
        {
            "$merge": {
                "into": "reports_user_courses",  # name of new collection
                "whenMatched": "replace",
                "whenNotMatched": "insert",
            }
        },
    ]

    # run aggregation
    collection.aggregate(pipeline)
    print("Aggregation complete! Results saved to 'reports_user_courses' collection.")

    # verification step — show saved results from new collection
    docs = db["reports_user_courses"].find()
    print("\n--- Contents of 'reports_user_courses' ---")
    for doc in docs:
        pp.pprint(doc)


# -------------------------
# Array Functions
# -------------------------

course_records_list = []
array = []


def array_of_documents():
    """Array to manipulate document"""
    print("-----Creating an array of documents-----")
    print("1. Add a new item to array ")
    print("2. Remove an item in array")
    print("3. Query array")
    print("4. Back to menu")
    choice = input("Enter choice: ")

    match choice:
        case "1":
            # find student in the database by id
            id = input("Enter student ID(e.g 'S10141'): ")

            # get info about the course you wann add from the user
            course_code = input("Enter course code(e.g'RDK439'): ")
            semester = input("Enter semester details(eg. 'Fall 2024'):")
            status = input("Enter status(e.g 'Enrolled'): ")
            grade = input("Enter a grade(e.g 'A'): ")

            # store them as a dict
            record = {
                "course_code": course_code,
                "semester": semester,
                "status": status,
                "grade": grade,
            }

            # find doc where student id matched the user's id
            student = collection.find_one({"student_id": id})

            # if you find student, update it  by adding a new record
            # and print the results
            array = collection.update_one(
                {"student_id": id}, {"$push": {"enrolled_courses": record}}
            )

            print("Successfully added to array")
            array_of_documents()

        case "2":
            print("1. Remove an enrolled course by course code: ")
            print("2. Remove all enrolled courses by student ID: ")
            choice = input("Enter choice: ")
            if choice == "1":
                id = input("Enter Student's ID: ")
                code = input("Enter course code: ")

                # if you find student, update it by removing a record
                # and print the results
                array = collection.update_one(
                    {"student_id": id},
                    {"$pull": {"enrolled_courses": {"course_code": code}}},
                )

            elif choice == "2":
                # get student id and course to remove and find that student
                id = input("Enter Student's ID: ")
                student = collection.find_one({"student_id": id})

                if not student:
                    print("Specified student id is invalid, Try Again")
                    array_of_documents()

                # if you find student, update it by removing all elements
                #  from enrolled courses and print the results
                array = collection.update_one(
                    {"student_id": id}, {"$pull": {"enrolled_courses": []}}
                )
            print("Successfully removed from array")
            array_of_documents()

        case "3":

            print("1. Find all students with the specified courses ")
            print("2. Find students with a specified size of courses")

            choice = input("Enter choice: ")

            if choice == "1":
                list = input(
                    "Enter course codes (leave blank spaces in between('CS9900 wr4909')): "
                ).split(" ")
                # find docs where array field contains all values in the list
                # and print results
                docs = collection.find({"enrolled_courses.course_code": {"$all": list}})
                for doc in docs:
                    pp.pprint(doc)

            elif choice == "2":
                num = int(input("Enter size of courses for a student: "))  # how?
                # get all students who have the number of courses
                # and print the results
                docs = collection.find({"enrolled_courses": {"$size": num}})
                for doc in docs:
                    pp.pprint(doc)

            array_of_documents()

        case "4":
            menu()
        case _:
            return "Invalid choice, try again"


# -------------------------
# Menu System
# -------------------------


def menu():
    while True:
        # print the menu header
        print()
        print("--- MongoDB Project Menu ---")
        print("1. Create Document")
        print("2. Create Document with ID")
        print("3. Create Many Documents")
        print("4. Read All Documents")
        print("5. Read Many Documents")
        print("6. Read First Document")
        print("7. Read Document by ID")
        print("8. Read Document by Criteria")
        print("9. Update Document by ID")
        print("10. Update Many Documents")
        print("11. Update Document")
        print("12. Delete Document by ID")
        print("13. Delete Document")
        print("14. Delete All Documents")
        print("15. Delete Many Documents")
        print("16. Perfom AND")
        print("17. Perfom OR")
        print("18. Perfom NOT")
        print("19. Array manipulation of documents")
        print("20. Comparison_operators")
        print("21. Match documents")
        print("22. Lookup aggregation")
        print("23. Lookup and merge aggregation")
        print("24. Exit")
        # reads user's menu choice
        choice = input("Enter choice (numeric): ")

        # call the functions according to what the user requested
        if choice == "1":
            create_document()

        elif choice == "2":
            create_document_with_id()

        elif choice == "3":
            create_many_documents()

        elif choice == "4":
            read_all_documents()

        elif choice == "5":
            read_many_documents()

        elif choice == "6":
            read_first_document()

        elif choice == "7":
            read_document_by_id()

        elif choice == "8":
            read_document_by_criteria()

        elif choice == "9":
            update_document_by_id()

        elif choice == "10":
            update_many_documents()

        elif choice == "11":
            update_document()

        elif choice == "12":
            delete_document_by_id()

        elif choice == "13":
            delete_document()

        elif choice == "14":
            delete_all_documents()

        elif choice == "15":
            delete_many_documents()

        elif choice == "16":
            and_function(collection)

        elif choice == "17":
            or_function(collection)

        elif choice == "18":
            not_function(collection)

        elif choice == "19":
            array_of_documents()

        elif choice == "20":
            comparison_operators(collection)

        elif choice == "21":
            match_documents()

        elif choice == "22":
            lookup_aggregation()

        elif choice == "23":
            lookup_and_merge_aggregation()

        # terminate program and break loop
        # else, print error message if input invalid
        elif choice == "24":
            print("Exiting...")
            quit()
            break

        else:
            print("Invalid choice, try again.")


# run the menu function when program starts
if __name__ == "__main__":
    menu()