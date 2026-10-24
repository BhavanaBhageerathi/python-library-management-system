# Python Library Management System

A terminal-based Library Management System developed using Python, Object-Oriented Programming (OOP), and MySQL. The application allows users to manage books, authors, categories, and book issuing and returning operations through an interactive command-line interface.

## Features

- **Add Author:** Add author records to the database.
- **Add Category:** Create categories for organizing books.
- **Add Book:** Add books with their titles, authors, categories, prices, and quantities.
- **View All Books:** Display book information, including author and category details.
- **Search Book:** Search for a book using its ID.
- **Update Book:** Update supported details of an existing book.
- **Delete Book:** Remove a book after confirmation.
- **Issue Book:** Perform book-issuing operations.
- **Return Book:** Handle book returns.
- **Input Validation:** Validate user inputs for supported operations.

## Technologies Used

- Python
- Object-Oriented Programming (OOP)
- MySQL
- MySQL Connector/Python
- SQL

## Project Structure

```text
python-library-management-system/
├── libmain.py
├── libdb.py
├── library_management_system_oops.sql
├── requirements.txt
├── README.md
├── .gitignore
└── screenshots/
    ├── main-menu.png
    ├── book-list.png
    └── book-management.png
```

## Prerequisites

- Python 3.10 or later
- MySQL Server
- A MySQL account with permission to create and modify the project database

## Installation and Setup

### 1. Download the Project

Clone the repository or download the project files from GitHub.

### 2. Install Dependencies

Open the project directory in VS Code and install the required packages:

```bash
python -m pip install -r requirements.txt
```

### 3. Configure Database Credentials

Create a local `.env` file in the project directory with your MySQL connection settings:

```text
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=library_management_system_oops
```

Replace the example password with your own MySQL password.

Do not commit the `.env` file to GitHub.

### 4. Set Up the Database

Ensure that MySQL Server is running and that the database `library_management_system_oops` exists.

The application defines the `AUTHORS`, `CATEGORIES`, and `BOOKS` tables in its table-creation logic.

Run the application after configuring the database connection. Confirm that the table-creation method is called during startup.

### 5. Run the Application

Run the main Python file:

```bash
python libmain.py
```

The application displays a menu for managing authors, categories, books, and book-issuing and returning operations.

## Screenshots

Screenshots demonstrating the application's interface and functionality will be added below.

### Main Menu

![Library Management System Main Menu](screenshots/main-menu.png)

### Book List

![Library Book List](screenshots/book-list.png)

### Book Management

![Library Book Management](screenshots/book-management.png)

## Future Enhancements

- Improve input validation and exception handling.
- Add a dedicated book-issue history.
- Introduce user authentication and role-based access control.
- Improve database connection management.
- Add reporting features for issued and available books.

## Author

Developed as a Python programming project.
