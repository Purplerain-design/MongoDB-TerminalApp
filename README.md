# MongoDB-TerminalApp

Project Overview:
MongoDB-TerminalApp is an interactive Python terminal application created by three students, it manages student information in a university database using MongoDB.

The dataset was generated with the Faker library to provide realistic random records. Our group focused on the student collection, which includes personal info, contact details, and arrays of enrolled courses. The app allows users to perform CRUD operations, advanced querying with logical operators, array manipulation for course enrollments, and aggregation pipelines to analyze student data.

# Tech tools:
- Python
- MongoDB
  
# How to run the app:
## First option (Local MongoDB)
- Create mongoDB account and make sure the server is running and use your connection string in the code to connect to mongoDB. [e.g. "client = MongoClient("mongodb://localhost:27017/")".]
- You can use Faker library to create university database with students collection.
- Install Conda, Open your terminal or Anaconda Prompt, create and activate a virtual environment
  
  <img width="777" height="80" alt="image" src="https://github.com/user-attachments/assets/f1282ec1-1fbf-4e9d-8aaa-d852dbf74111" />

### Install dependencies:
Use **pip** to install these python packages and when you done you can run **pip list** or **conda list**  it will show you the installed packages and their
respective versions.
- pymongo → Python driver for MongoDB (used to read/export data if needed).
- pytest → Run unit tests.
- ipytests → Run unit test in notebooks.
- black → Code formatter to maintain consistent style.
- black[jupyter] → Code formatter for notebooks.
- jupyter → Interactive notebooks.
- Run "python app.py" on the terminal and make sure you're in the right directory. you will see an output similar to the screenshot below.
  
<img width="940" height="560" alt="image" src="https://github.com/user-attachments/assets/9952cce4-bfe8-4ce2-b666-4cb0fd550184" />

## Second option ( MongoDB Atlas)
- Create MongoDB Atlas account, create a cluster and a university database with a students collection. In the code, replace "client = MongoClient("mongodb://localhost:27017/")" with your Atlas login credentials(get the URL from mongodb).
- You can use Faker library to create university database with students collection.
- Install Conda, Open your terminal or Anaconda Prompt, create and activate a virtual environment
  
  <img width="777" height="80" alt="image" src="https://github.com/user-attachments/assets/f1282ec1-1fbf-4e9d-8aaa-d852dbf74111" />

### Install dependencies:
Use **pip** to install these python packages and when you done you can run **pip list** or **conda list**  it will show you the installed packages and their
respective versions.
- pymongo → Python driver for MongoDB (used to read/export data if needed).
- pytest → Run unit tests.
- ipytests → Run unit test in notebooks.
- black → Code formatter to maintain consistent style.
- black[jupyter] → Code formatter for notebooks.
- jupyter → Interactive notebooks.
- Run "python app.py" on the terminal and make sure you're in the right directory. you will see an output similar to the screenshot below.
  
<img width="940" height="560" alt="image" src="https://github.com/user-attachments/assets/9952cce4-bfe8-4ce2-b666-4cb0fd550184" />

