# MongoDB-TerminalApp

Project Overview:
MongoDB-TerminalApp is an interactive Python terminal application created by three students, it manages student information in a university database using MongoDB.

The dataset was generated with the Faker library to provide realistic random records. Our group focused on the student collection, which includes personal info, contact details, and arrays of enrolled courses. The app allows users to perform CRUD operations, advanced querying with logical operators, array manipulation for course enrollments, and aggregation pipelines to analyze student data.

# How to run the app:
# First option (Local MongoDB)
- Install mongoDB and make sure the server is running and use your connection string in the code. "client = MongoClient("mongodb://localhost:27017/")".
- You can use Faker library to create university database with students collection.
- Install Conda, create and activate a virtual environment
- Install dependencies
- Run "python app.py" on the terminal and make sure you're in the right directory.

# Second option ( MongoDB Atlas)
- Create MongoDB Atlas account, create a cluster and a university database with a students collection. In the code, replace "client = MongoClient("mongodb://localhost:27017/")" with your Atlas login credentials.
- You can use Faker library to create university database with students collection.
- Install Conda, create and activate a virtual environment
- Install dependencies
- Run "python app.py" on the terminal and make sure you're in the right directory.
