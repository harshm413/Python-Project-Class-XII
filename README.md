# Python Project Class XII
## Computer Science 
## LIBRARY MANAGEMENT PROJECT
## PYTHON-MYSQL CONNECTIVITY
## 2020-21
 
# Library Management System

## Introduction
Library Management System is a software used to manage the catalog of a library. It helps in keeping records of the books available in the library and managing the transactions related to issuing and returning books. This system provides features to add, delete, update, and view book and student records, as well as tracking the current status and history of book transactions.

## Features
- Keep records of books available in the library
- Maintain student records
- Issue books to students and prevent multiple issuances of the same book
- Enforce a single book issuance per student
- Verify book returns and ensure they match the issued books
- Calculate fines for late book returns
- Add, delete, update, and view book and student records
- View a list of students currently holding books from the library
- Capture the history of book issuances and submissions
- And more

## Tables in MySQL
The project uses the following tables in MySQL:

### book
- Fields:
  - bno: varchar(5) (Primary Key)
  - bname: varchar(20)

### student
- Fields:
  - sno: varchar(6) (Primary Key)
  - sname: varchar(25)

### current
- Fields:
  - sno: varchar(6) (Primary Key)
  - sname: varchar(25)
  - bno: varchar(5)
  - bname: varchar(20)
  - date: varchar(10)

### history
- Fields:
  - action: varchar(10)
  - sno: varchar(6)
  - sname: varchar(25)
  - bno: varchar(5)
  - bname: varchar(20)
  - date: varchar(10)

## Functions in Python
The project includes the following functions:

- `main()`: The main entry point of the program.
- `password()`: Asks the user for a password.
- `dispcurrent()`: Displays the records in the current table from MySQL.
- `disphistory()`: Displays the records in the history table from MySQL.
- `admin()`: Leads to the admin block to add, delete, update, or display records of books or students.
- `books()`: Accessed from the admin menu to add, delete, update, or display records of books.
- `students()`: Accessed from the admin menu to add, delete, update, or display records of students.
- `add(obj)`: Adds a record to the book or student list in MySQL, depending on the `obj` argument.
- `delete(obj)`: Deletes a record from the book or student list in MySQL, depending on the `obj` argument.
- `update(obj)`: Updates a record in the book or student list in MySQL, depending on the `obj` argument.
- `disp(obj)`: Shows records from the book or student list in MySQL, depending on the `obj` argument.
- `issue()`: Issues a book from the library to a student.
- `submit()`: Submits a book to the library from a student.

## Usage
1. Make sure you have MySQL installed and running.
2. Create a database named `lib`.
3. Create the required tables (`book`, `student`, `current`, `history`) in the `lib` database.
4. Update the MySQL connection details in the code (host, user, password, database).
5. Run the program and follow the prompts to perform different actions in the Library Management System.

## License
This project is licensed under the [MIT License](LICENSE).