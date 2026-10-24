import mysql.connector


class Database:

    def __init__(self):
        self.dbobj = mysql.connector.connect(
            host="localhost",
            user="root",
            password="admin123",
            database="library_management_system_oops"
        )

        self.dbcursor = self.dbobj.cursor()


database = Database()





class Tables:

    def table_creation(self):
        #AUTHORS TABLE
        myquery = """
        CREATE TABLE IF NOT EXISTS AUTHORS(
            AUTHOR_ID INT PRIMARY KEY AUTO_INCREMENT,
            AUTHOR_NAME VARCHAR(100))
        """
        database.dbcursor.execute(myquery)
        database.dbobj.commit()

        #CATEGORIES TABLE
        myquery = """
        CREATE TABLE IF NOT EXISTS CATEGORIES(
            CATEGORY_ID INT PRIMARY KEY AUTO_INCREMENT,
            CATEGORY_NAME VARCHAR(500))
        """
        database.dbcursor.execute(myquery)
        database.dbobj.commit()

        #BOOKS TABLE
        myquery = """
        CREATE TABLE IF NOT EXISTS BOOKS(
            BOOK_ID INT PRIMARY KEY AUTO_INCREMENT,
            TITLE VARCHAR(150),
            AUTHOR_ID INT,
            CATEGORY_ID INT,
            PRICE DECIMAL(10,2),
            QUANTITY INT,
            FOREIGN KEY(AUTHOR_ID) REFERENCES AUTHORS(AUTHOR_ID),
            FOREIGN KEY(CATEGORY_ID) REFERENCES CATEGORIES(CATEGORY_ID)
        )
        """
        database.dbcursor.execute(myquery)
        database.dbobj.commit()


class Libraryapp:

    def show_menu(self):

        while True:

            print("""
+----------------------------------------+
|      LIBRARY MANAGEMENT SYSTEM         |
+----------------------------------------+
""")

            print("""
1. Add Author
2. Add Category
3. Add Book
4. View All Books
5. Search Book
6. Update Book
7. Delete Book
8. Issue Book
9. Return Book
10. Exit
""")

            self.run()

    def run(self):

        choice = input("Enter choice : ").strip()

        if choice == "1":
            Author().add_author()

        elif choice == "2":
            Category().add_category()

        elif choice == "3":
            Book().add_book()

        elif choice == "4":
            Book().view_books()

        elif choice == "5":
            Book().search_book()

        elif choice == "6":
            Book().update_book()

        elif choice == "7":
            Book().delete_book()

        elif choice == "8":
            Book().issue_book()

        elif choice == "9":
            Book().return_book()

        elif choice == "10":
            print("THANKYOU..")
            exit()

        else:
            print("Invalid Choice")


class Author:


    def add_author(self):

        while True:
            print('''TYPE 'back' TO RETURN''')
            author_name = input("Enter Author Name  : ").strip()

            if author_name.lower() == "back":
                return

            #empty validation
            if author_name == "":
                print("Author name cannot be empty.")
                continue

            #author duplicate validation
            myquery = "SELECT * FROM AUTHORS WHERE AUTHOR_NAME = %s"
            database.dbcursor.execute(myquery, (author_name,))
            myresult = database.dbcursor.fetchone()

            if myresult:
                print("Author already exists.")
                continue

            #inserting author
            myquery = "INSERT INTO AUTHORS(AUTHOR_NAME) VALUES(%s)"
            database.dbcursor.execute(myquery, (author_name,))
            database.dbobj.commit()

            print("----------------------------")
            print("Author added successfully.")
            print("----------------------------")

            self.view_authors()
            return



    def view_authors(self):

        myquery = "SELECT * FROM AUTHORS"
        database.dbcursor.execute(myquery)
        myresult = database.dbcursor.fetchall()

        if not myresult:
            print("No authors found.")
            return

        for eachrow in myresult:
            print("AUTHOR_ID   :", eachrow[0])
            print("AUTHOR_NAME :", eachrow[1])
            print("--------------------------")

       
        



class Category:

    def add_category(self):

        while True:
            print('''TYPE 'back' TO RETURN''')
            category_name = input("Enter Category Name : ").strip()

            if category_name.lower() == "back":
                return

            #empty validation
            if category_name == "":
                print("Category name cannot be empty.")
                continue

            #category duplicate validation
            myquery = "SELECT * FROM CATEGORIES WHERE CATEGORY_NAME = %s"
            database.dbcursor.execute(myquery, (category_name,))
            myresult = database.dbcursor.fetchone()

            if myresult:
                print("Category already exists.")
                continue

            #inserting category
            myquery = "INSERT INTO CATEGORIES(CATEGORY_NAME) VALUES(%s)"
            database.dbcursor.execute(myquery, (category_name,))
            database.dbobj.commit()

            print("----------------------------")
            print("Category added successfully.")
            print("----------------------------")

            self.view_category()
            return



    def view_category(self):

        myquery = "SELECT * FROM CATEGORIES"
        database.dbcursor.execute(myquery)
        myresult = database.dbcursor.fetchall()

        if not myresult:
            print("No categories found.")
            return

        for eachrow in myresult:
            print("CATEGORY_ID   :", eachrow[0])
            print("CATEGORY_NAME :", eachrow[1])
            print("--------------------------")
        





class Book:

    def add_book(self):

        while True:
            print('''TYPE 'back' TO RETURN''')
            title = input("Enter Book Title  : ").strip()

            if title.lower() == "back":
                return

            #empty title validation
            if title == "":
                print("Book title cannot be empty.")
                continue
            break

        #choose authors

        while True:
            print("\n****Available Authors****")

            myquery = "SELECT * FROM AUTHORS"
            database.dbcursor.execute(myquery)
            myqueryresult = database.dbcursor.fetchall()

            if not myqueryresult:  #if no atleast one authors in table
                print("No authors found. Please add an author first.")
                return

            for eachrow in myqueryresult: #if rows are there print
                print("AUTHOR_ID:", eachrow[0], "-", "AUTHOR_NAME:", eachrow[1])

            print('''TYPE 'back' TO RETURN''') #typing id
            author_id = input("Enter Author ID  : ").strip()

            if author_id.lower() == "back":
                return

            myquery = "SELECT * FROM AUTHORS WHERE AUTHOR_ID=%s"  #checking if typed id exists
            database.dbcursor.execute(myquery, (author_id,))
            myqueryresult = database.dbcursor.fetchone()

            if not myqueryresult:
                print("Invalid Author ID.")
                continue

            break


        #choose categories
        while True:

            print("\n****Available Categories****")  #listing all available categories

            myquery = "SELECT * FROM CATEGORIES"
            database.dbcursor.execute(myquery)
            myqueryresult = database.dbcursor.fetchall()

            if not myqueryresult: #if no atleast one row
                print("No categories found. Please add a category first.")
                return

            for eachrow in myqueryresult: #list the rows
                print("CATEGORY_ID:", eachrow[0], "-", "CATEGORY_NAME:", eachrow[1])

            print('''TYPE 'back' TO RETURN''')
            category_id = input("Enter Category ID  : ").strip() #typein category id

            if category_id.lower() == "back":
                return

            myquery = "SELECT * FROM CATEGORIES WHERE CATEGORY_ID=%s" #if categoryid exists
            database.dbcursor.execute(myquery, (category_id,))
            myqueryresult = database.dbcursor.fetchone()

            if not myqueryresult:
                print("Invalid Category ID.")
                continue

            break


        #price validation
        while True:

            print('''TYPE 'back' TO RETURN''')
            price = input("Enter Price: ").strip() #inputing price
            if price.lower() == "back":
                return

            try:
                price = float(price)
                if price <= 0:
                    print("Price must be greater than 0.")
                    continue
                break

            except:
                print("Invalid Price.")


        #quantity validation
        while True:

            print('''TYPE 'back' TO RETURN''')
            quantity = input("Enter Quantity  : ").strip() #inputing quantity

            if quantity.lower() == "back":
                return

            try:

                quantity = int(quantity)

                if quantity < 0:
                    print("Quantity cannot be negative.")
                    continue

                break

            except:
                print("Invalid Quantity.")


        #inserting into books table
        myquery = """
        INSERT INTO BOOKS
        (TITLE,AUTHOR_ID,CATEGORY_ID,PRICE,QUANTITY)
        VALUES(%s,%s,%s,%s,%s)
        """

        values = (title, author_id, category_id, price, quantity)

        database.dbcursor.execute(myquery, values)
        database.dbobj.commit()

        print("----------------------------")
        print("Book added successfully.")
        print("----------------------------")










    def view_books(self):
        
    
        #joining category,authors and books table
        myquery = """
        SELECT BOOKS.BOOK_ID,BOOKS.TITLE,AUTHORS.AUTHOR_NAME,CATEGORIES.CATEGORY_NAME,BOOKS.PRICE,BOOKS.QUANTITY
        FROM BOOKS INNER JOIN AUTHORS
        ON BOOKS.AUTHOR_ID = AUTHORS.AUTHOR_ID
        INNER JOIN CATEGORIES
        ON BOOKS.CATEGORY_ID = CATEGORIES.CATEGORY_ID
        """
        database.dbcursor.execute(myquery)
        myresult = database.dbcursor.fetchall()

        if not myresult: #if no books present already
            print("No books found.")
            return

        print("---------------------------------------------------------------------------------")
        print("{:<5} {:<20} {:<20} {:<15} {:<8} {:<5}".format("ID", "Title", "Author", "Category", "Price", "Qty"))
        print("---------------------------------------------------------------------------------")

        for eachrow in myresult:
            print("{:<5} {:<20} {:<20} {:<15} {:<8} {:<5}".format(eachrow[0],eachrow[1],eachrow[2],eachrow[3],eachrow[4],eachrow[5]))

        print("---------------------------------------------------------------------------------")






    def search_book(self):

        while True:

            #entering book id
            print('''TYPE 'back' TO RETURN''')
            book_id = input("Enter Book ID  : ").strip()

            if book_id.lower() == "back":
                return

            if book_id == "": #empty validation
                print("Book ID cannot be empty.")
                continue

            #searching book using book id
            myquery = """
            SELECT BOOKS.TITLE,AUTHORS.AUTHOR_NAME,CATEGORIES.CATEGORY_NAME,BOOKS.PRICE,BOOKS.QUANTITY
            FROM BOOKS INNER JOIN AUTHORS
            ON BOOKS.AUTHOR_ID = AUTHORS.AUTHOR_ID
            INNER JOIN CATEGORIES
            ON BOOKS.CATEGORY_ID = CATEGORIES.CATEGORY_ID
            WHERE BOOKS.BOOK_ID = %s
            """

            database.dbcursor.execute(myquery, (book_id,))
            myresult = database.dbcursor.fetchone()

            if not myresult:   #if book not found with that id
                print("-----------------")
                print("Book not found.")
                print("-----------------")
                continue

            print("\nBook Details") #if found:
            print("---------------------------")
            print("Title    :", myresult[0])
            print("Author   :", myresult[1])
            print("Category :", myresult[2])
            print("Price    :", myresult[3])
            print("Quantity :", myresult[4])
            print("----------------------------")

            return




    def update_book(self):

        while True:

            #searching with book id
            print('''TYPE 'back' TO RETURN''')
            book_id = input("Enter Book ID  : ").strip()

            if book_id.lower() == "back":
                return

            if book_id == "":
                print("Book ID cannot be empty.")
                continue

            myquery = "SELECT * FROM BOOKS WHERE BOOK_ID=%s"
            database.dbcursor.execute(myquery, (book_id,))
            myresult = database.dbcursor.fetchone()

            if not myresult:  #if no book with that id found:
                print("-----------------")
                print("Book not found.")
                print("-----------------")
                continue

            break


        while True: #if book with that id found:

            print("""What do you want to update?
                    1. Category
                    2. Price
                    3. Quantity
                    Type 'back' to return.""")

            choice = input("Enter your choice : ").strip().lower()

            if choice == "back":
                return

            if choice == "1":

                while True:

                    #to choose categories
                    print("\n****Available Categories****")

                    myquery = "SELECT * FROM CATEGORIES"
                    database.dbcursor.execute(myquery)
                    myresult = database.dbcursor.fetchall()

                    for eachrow in myresult:
                        print("CATEGORY_ID:", eachrow[0], "-", "CATEGORY_NAME:", eachrow[1])

                    #entering new category
                    print('''TYPE 'back' TO RETURN''')
                    category_id = input("Enter New Category ID  : ").strip()

                    if category_id.lower() == "back":
                        return

                    myquery = "SELECT * FROM CATEGORIES WHERE CATEGORY_ID=%s"  #checking if typed category is valid
                    database.dbcursor.execute(myquery, (category_id,))
                    myresult = database.dbcursor.fetchone()

                    if not myresult:
                        print("Invalid Category ID.")
                        continue

                    myquery = "UPDATE BOOKS SET CATEGORY_ID=%s WHERE BOOK_ID=%s" #if valid:
                    database.dbcursor.execute(myquery, (category_id, book_id))
                    database.dbobj.commit()

                    print("----------------------------")
                    print("Book updated successfully.")
                    print("----------------------------")
                    return


            elif choice == "2":

                while True:

                    print('''TYPE 'back' TO RETURN''')
                    price = input("Enter New Price  : ").strip()

                    if price.lower() == "back":
                        return

                    try:

                        price = float(price)

                        if price <= 0:
                            print("Price must be greater than 0.")
                            continue

                        myquery = "UPDATE BOOKS SET PRICE=%s WHERE BOOK_ID=%s"
                        database.dbcursor.execute(myquery, (price, book_id))
                        database.dbobj.commit()

                        print("----------------------------")
                        print("Book updated successfully.")
                        print("----------------------------")
                        return

                    except:
                        print("Invalid Price.")


            elif choice == "3":

                while True:
                    print('''TYPE 'back' TO RETURN''')
                    quantity = input("Enter New Quantity: ").strip()

                    if quantity.lower() == "back":
                        return

                    try:

                        quantity = int(quantity)

                        if quantity < 0:
                            print("Quantity cannot be negative.")
                            continue

                        myquery = "UPDATE BOOKS SET QUANTITY=%s WHERE BOOK_ID=%s"
                        database.dbcursor.execute(myquery, (quantity, book_id))
                        database.dbobj.commit()

                        print("----------------------------")
                        print("Book updated successfully.")
                        print("----------------------------")
                        return

                    except:
                        print("Invalid Quantity.")

            else:
                print("Invalid Choice.")











    def delete_book(self):

        while True:

            #searching with book id
            print('''TYPE 'back' TO RETURN''')
            book_id = input("Enter Book ID  : ").strip()

            if book_id.lower() == "back":
                return

            if book_id == "":
                print("Book ID cannot be empty.")
                continue

            myquery = "SELECT * FROM BOOKS WHERE BOOK_ID=%s"
            database.dbcursor.execute(myquery, (book_id,))
            myresult = database.dbcursor.fetchone()

            if not myresult:   #if book not existing
                print("-----------------")
                print("Book not found.")
                print("-----------------")
                continue

            break


        while True:

            #confirmation
            print('''TYPE 'back' TO RETURN''')
            choice = input("Are you sure (Y/N)?  : ").strip().upper()

            if choice.lower() == "back":
                return

            if choice == "Y":

                myquery = "DELETE FROM BOOKS WHERE BOOK_ID=%s"
                database.dbcursor.execute(myquery, (book_id,))
                database.dbobj.commit()

                print("----------------------------")
                print("Book deleted successfully.")
                print("----------------------------")
                return

            elif choice == "N":

                print("Book deletion cancelled.")
                return

            else:

                print("Invalid Choice.")






    def issue_book(self):

        while True:

            #searching with book id
            print('''TYPE 'back' TO RETURN''')
            book_id = input("Enter Book ID  : ").strip()

            if book_id.lower() == "back":
                return

            if book_id == "":
                print("Book ID cannot be empty.")
                continue

            myquery = "SELECT * FROM BOOKS WHERE BOOK_ID=%s"
            database.dbcursor.execute(myquery, (book_id,))
            myresult = database.dbcursor.fetchone()

            if not myresult:   #if that book id does not exist
                print("-----------------")
                print("Book not found.")
                print("-----------------")
                continue

            #checking quantity
            quantity = myresult[5]

            if quantity <= 0:
                print("---------------------")
                print("Book is out of stock.")
                print("---------------------")
                continue

            #reducing quantity by 1 so issued
            new_quantity = quantity - 1

            myquery = "UPDATE BOOKS SET QUANTITY=%s WHERE BOOK_ID=%s"
            database.dbcursor.execute(myquery, (new_quantity, book_id))
            database.dbobj.commit()

            print("----------------------------")
            print("Book issued successfully.")
            print("Remaining Quantity :", new_quantity)
            print("----------------------------")

            return


            

    def return_book(self):

        while True:

            #searching with book id
            print('''TYPE 'back' TO RETURN''')
            book_id = input("Enter Book ID  : ").strip()

            if book_id.lower() == "back":
                return

            if book_id == "":
                print("Book ID cannot be empty.")
                continue

            myquery = "SELECT * FROM BOOKS WHERE BOOK_ID=%s"
            database.dbcursor.execute(myquery, (book_id,))
            myresult = database.dbcursor.fetchone()

            if not myresult:   #if that book id is not existing
                print("-----------------")
                print("Book not found.")
                print("-----------------")
                continue

            #increasing quantity by 1 after return
            quantity = myresult[5]
            new_quantity = quantity + 1

            myquery = "UPDATE BOOKS SET QUANTITY=%s WHERE BOOK_ID=%s"
            database.dbcursor.execute(myquery, (new_quantity, book_id))
            database.dbobj.commit()

            print("----------------------------")
            print("Book returned successfully.")
            print("Current Quantity :", new_quantity)
            print("----------------------------")

            return















Tables().table_creation()

Libraryapp().show_menu()

