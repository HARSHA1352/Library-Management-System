# Library-Management-System

This project consists of two Python files: LMS.py and database.py. The LMS.py file contains the implementation of a Library Management System, while the database.py file provides a simple database class for storing user and book information.

## LMS.py
The LMS.py file is responsible for the main functionality of the Library Management System. It allows users to log in as either a manager or a customer and perform various operations based on their role.

## Classes
LibraryManagementSystem: Represents the Library Management System. It takes the user's username, password, and type (manager or customer) during initialization. It authenticates the user and provides a menu for performing different operations based on the user's type.

## Methods
- _authenticate: Authenticates the user by checking the provided username, password, and type against the database.
- _printMenu: Displays the menu options based on the user's type and allows the user to choose an operation.
- Other methods in the LibraryManagementSystem class correspond to different operations available to managers and customers.

## database.py
The database.py file contains a simple Database class that serves as the data storage for the Library Management System. It stores information about managers, customers, and books.

## Classes
Database: Represents the database for the Library Management System. It contains sets to store manager data, customer data, and books.

## Methods
- _isvalid: Checks if the provided username, password, and type exist in the corresponding data set (manager or customer).
- Methods like _AddNewBook, _isAvailable, _viewSpecificBook, _viewAllBooks, _RemoveBooks, _UpdateBookDetails, _GenerateInvoice, _RentBook, _payBill, and _AcceptPayment perform specific operations on the database, such as adding a new book, viewing book details, removing a book, updating book details, and more.

## Usage
- When prompted, choose whether you want to log in, sign up, or exit the system.
- If you choose to log in, enter your username, password, and type (1 for manager or 2 for customer).
- Once logged in, you will see a menu with available options based on your role.
- Select an option by entering the corresponding number.
- Follow the prompts to perform the desired operation.
