import java.util.Scanner;

public class LibraryManagementSystem {
    public static void main(String[] args) {
        Library library = new Library();
        Scanner scanner = new Scanner(System.in);

        // Adding some sample data
        library.addBook("The Alchemist", "Paulo Coelho");
        library.addBook("1984", "George Orwell");
        library.addUser("Alice");
        library.addUser("Bob");

        // Main menu
        while (true) {
            System.out.println("\nLibrary Management System");
            System.out.println("1. Display Books");
            System.out.println("2. Add Book");
            System.out.println("3. Add User");
            System.out.println("4. Issue Book");
            System.out.println("5. Return Book");
            System.out.println("6. Exit");
            System.out.print("Enter your choice: ");
            int choice = scanner.nextInt();

            switch (choice) {
                case 1 -> library.displayBooks();
                case 2 -> {
                    scanner.nextLine(); // Consume newline
                    System.out.print("Enter book title: ");
                    String title = scanner.nextLine();
                    System.out.print("Enter book author: ");
                    String author = scanner.nextLine();
                    library.addBook(title, author);
                }
                case 3 -> {
                    scanner.nextLine(); // Consume newline
                    System.out.print("Enter user name: ");
                    String name = scanner.nextLine();
                    library.addUser(name);
                }
                case 4 -> {
                    System.out.print("Enter book ID to issue: ");
                    int issueId = scanner.nextInt();
                    library.issueBook(issueId);
                }
                case 5 -> {
                    System.out.print("Enter book ID to return: ");
                    int returnId = scanner.nextInt();
                    library.returnBook(returnId);
                }
                case 6 -> {
                    System.out.println("Exiting system. Goodbye!");
                    scanner.close();
                    return;
                }
                default -> System.out.println("Invalid choice. Try again.");
            }
        }
    }
}
