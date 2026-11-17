class Book:
    def __init__(self, title):
        self.title = title
        self.available = True
    def issue(self):
        if self.available:
            self.available = False
            print("Book issued successfully!")
        else:
            print("Book is not available!")
    def return_book(self):
        if not self.available:
            self.available = True
            print("Book returned successfully!")
        else:
            print("Book was not issued!")
    def display(self):
        status = "Available" if self.available else "Issued"
        print(self.title, "-", status)
# Create books
books = [
    Book("Python Programming"),
    Book("Java Programming"),
    Book("Data Structures")
]
while True:
    print("\n1. Display Books")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        for book in books:
            book.display()
    elif choice == "2":
        title = input("Enter book title: ")
        for book in books:
            if book.title.lower() == title.lower():
                book.issue()
                break
        else:
            print("Book not found!")
    elif choice == "3":
        title = input("Enter book title: ")
        for book in books:
            if book.title.lower() == title.lower():
                book.return_book()
                break
        else:
            print("Book not found!")
    elif choice == "4":
        print("Exiting Library System!")
        break
    else:
        print("Invalid choice!")
