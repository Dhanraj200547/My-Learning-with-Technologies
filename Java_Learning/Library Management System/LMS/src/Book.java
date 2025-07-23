class Book {
     int id;
     String title;
     String author;
     boolean isIssued;

    // Constructor
    public Book(int id, String title, String author) {
        this.id = id;
        this.title = title;
        this.author = author;
        this.isIssued = false;
    }

    // Getters and Setters (Encapsulation)
    public int getId() {
        return id;
    }

    public String getTitle() {
        return title;
    }

    public String getAuthor() {
        return author;
    }

    public boolean isIssued() {
        return isIssued;
    }

    public void issueBook() {
        if (!isIssued) {
            isIssued = true;
            System.out.println("Book '" + title + "' issued successfully.");
        } else {
            System.out.println("Book '" + title + "' is already issued.");
        }
    }

    public void returnBook() {
        if (isIssued) {
            isIssued = false;
            System.out.println("Book '" + title + "' returned successfully.");
        } else {
            System.out.println("Book '" + title + "' was not issued.");
        }
    }
}
