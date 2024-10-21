'''
                                    LIBRARY MANAGEMENT SYSTEM
'''

class Library:

    # DICTIONARY OF AVAILABLE BOOKS WITH ITS QUANTITY AND ISSUED BOOKS AND A DICTIONARY FOR ISSUED BOOKS
    def __init__(self):
        
        self.books = {
            "Scripting Language Python": 3,
            "Data Structures and Algorithms": 2,
            "Responsive Webpage Design": 1,
            "Basic Operating System": 4,
            "Relational Database Management System": 2
        }

        self.issuedBooks = {}


    # DISPLAY ALL AVAILABLE BOOKS
    def displayBooks(self):

        print("\nAvailable Books:")

        for book, qty in self.books.items():
            if qty > 0:
                print(f"{book} - {qty} copies")

        print("\n")


    # ADD A NEW BOOK TO THE LIBRARY
    def addBook(self, bookName, quantity):

        if bookName in self.books:
            self.books[bookName] += quantity

        else:
            self.books[bookName] = quantity

        print(f"{quantity} copies of '{bookName}' added to the library.\n")


    # ISSUE A BOOK TO A STUDENT
    def issueBook(self, bookName, studentName):

        if bookName in self.books and self.books[bookName] > 0:
            self.books[bookName] -= 1
            self.issuedBooks[studentName] = bookName
            print(f"Book '{bookName}' issued to {studentName}.\n")
            
        else:
            print(f"Sorry, '{bookName}' is not available right now.\n")


    # RETURN A PREVIOUSLY ISSUED BOOK
    def returnBook(self, studentName):

        if studentName in self.issuedBooks:
            bookName = self.issuedBooks[studentName]
            self.books[bookName] += 1
            print(f"Book '{bookName}' returned by {studentName}.\n")
            del self.issuedBooks[studentName]

        else:
            print(f"No book has been issued to {studentName}.\n")


    # DISPLAY ISSUED BOOKS BY A STUDENT
    def viewIssuedBooks(self):

        print("\nIssued Books:")

        if len(self.issuedBooks) > 0:
            for student, book in self.issuedBooks.items():
                print(f"{book} issued to {student}")

        else:
            print("No books are currently issued.")

        print("\n")

def main():
    library = Library()

    # LIBRARY MENU OPTIONS
    while True:

        print("\n--- Library Management System ---")
        print("1. Display Available Books")
        print("2. Add New Book")
        print("3. Issue Book to Student")
        print("4. Return Book")
        print("5. View Issued Books")
        print("6. Exit")
        
        choice = int(input("Enter your choice: "))

        if choice == 1:
            library.displayBooks()
        
        elif choice == 2:
            bookName = input("Enter the name of the book to add: ")
            quantity = int(input("Enter the quantity: "))
            library.addBook(bookName, quantity)
        
        elif choice == 3:
            studentName = input("Enter the student's name: ")
            bookName = input("Enter the name of the book to issue: ")
            library.issueBook(bookName, studentName)
        
        elif choice == 4:
            studentName = input("Enter the student's name: ")
            library.returnBook(studentName)
        
        elif choice == 5:
            library.viewIssuedBooks()

        elif choice == 6:
            print("THANK YOU!")
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()