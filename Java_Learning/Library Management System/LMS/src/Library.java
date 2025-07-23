import java.util.ArrayList;

class Library {
     static int bookCount = 0; // Static counter for books
    
     ArrayList<Book> books = new ArrayList<>(); // List of books
    
     ArrayList<User> users = new ArrayList<>(); // List of users

    // Add a new book to the library
    public void addBook(String title, String author) {
        Book newBook = new Book(++bookCount, title, author);
        books.add(newBook);
        System.out.println("Book added: " + title);
    }

    // Add a new user to the library
    public void addUser(String name) {
        User newUser = new User(users.size() + 1, name);
        users.add(newUser);
        System.out.println("User added: " + name);
    }

    // Display all books
    public void displayBooks() {
        System.out.println("\nLibrary Books:");
        for (Book book : books) {
            System.out.println("ID: " + book.getId() + ", Title: " + book.getTitle() + ", Author: " + book.getAuthor() + ", Issued: " + (book.isIssued() ? "Yes" : "No"));
        }
    }

    // Issue a book
    public void issueBook(int bookId) {
        for (Book book : books) {
            if (book.getId() == bookId) {
                book.issueBook();
                return;
            }
        }
        System.out.println("Book ID " + bookId + " not found.");
    }

    // Return a book
    public void returnBook(int bookId) {
        for (Book book : books) {
            if (book.getId() == bookId) {
                book.returnBook();
                return;
            }
        }
        System.out.println("Book ID " + bookId + " not found.");
    }
}
