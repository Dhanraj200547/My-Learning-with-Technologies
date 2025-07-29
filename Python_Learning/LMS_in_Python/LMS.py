from Library import Library

def main():
    import sys
    library = Library()

    # Add default books and users
    library.addBook("Wings of Fire", "Dr. A.P.J. Abdul Kalam")
    library.addBook("2011", "Shastri")
    library.addUser("Dhanraj")
    library.addUser("Max")
    while True:
        print("\n===== Library Management System =====")
        print("1. Display Books")
        print("2. Add Book")
        print("3. Add User")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Exit")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("❗ Invalid input. Enter a number.")
            continue

        if choice == 1:
            library.displaybooks()
        elif choice == 2:
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            library.addBook(title, author)
        elif choice == 3:
            name = input("Enter user name: ")
            library.addUser(name)
        elif choice == 4:
            try:
                book_id = int(input("Enter book ID to issue: "))
                library.issueBook(book_id)
            except ValueError:
                print("❗ Invalid ID.")
        elif choice == 5:
            try:
                book_id = int(input("Enter book ID to return: "))
                library.returnBook(book_id)
            except ValueError:
                print("❗ Invalid ID.")
        elif choice == 6:
            print(" Exiting Library System.")
            sys.exit()
        else:
            print("❗ Invalid choice. Try again.")


if __name__ == "__main__":
    main()
