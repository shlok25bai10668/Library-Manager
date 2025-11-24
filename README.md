# Library-Manager
Library Management System Overview

A Python-based Library Management System using MySQL for database operations. Features include adding books, viewing all records, searching by category, and removing books. Built with mysql-connector-python and tabulate for clean console output. Ideal for learning database connectivity and CRUD operations in Python projects.
Features
Add Books: Store new book records with title, author, publishing date, publisher, and category View All Books: Display all library records in a formatted table Search by Category: Filter and display books by their category Remove Books: Delete book records by title User-Friendly Interface: Simple menu-driven console application
Technologies Used
Python 3.x: Core programming language MySQL Server: Database management system mysql-connector-python: Python-MySQL connectivity tabulate: Library for formatting console tables
Prerequisites Before running this project, ensure you have:
Python 3.x installed MySQL Server installed and running Required Python packages installed
Installation Step 1: Clone the Repository
git clone https://github.com/yourusername/library-management-system.git cd library-management-system
Step 2: Install Required Packages pip install mysql-connector-python tabulate
Step 3: Configure MySQL
Ensure MySQL server is running on localhost with root access. You'll be prompted for your MySQL password when running the application.
Usage Running the Application
python library_management.py Menu Options
1. View books - Display all books in the library 2. Add book - Add a new book record 3. Remove book - Delete a book by title 4. Search by Category - Find books in a specific category 5. Exit - Close the application
Example Workflow
1. Run the script and enter your MySQL password 2. Choose option 2 to add books 3. Enter book details when prompted 4. Use option 1 to view all added books 5. Use option 4 to search by category
