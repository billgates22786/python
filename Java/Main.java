import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Create a library with a capacity for 100 books and 100 members
        Library library = new Library(100, 100);
        int choice;

        do {
            System.out.println("\nLibrary Management System");
            System.out.println("1. Add Book");
            System.out.println("2. Register Member");
            System.out.println("3. Borrow Book");
            System.out.println("4. Return Book");
            System.out.println("0. Exit");
            System.out.print("Enter your choice: ");
            choice = scanner.nextInt();
            scanner.nextLine(); // Consume newline character after nextInt()

            switch (choice) {
                case 1:
                    library.addBook();
                    break;
                case 2:
                    library.registerMember();
                    break;
                case 3:
                    library.borrowBook();
                    break;
                case 4:
                    library.returnBook();
                    break;
                case 0:
                    System.out.println("Exiting Library Management System. Goodbye!");
                    break;
                default:
                    System.out.println("Invalid choice. Please enter a number from the menu.");
                    break;
            }
        } while (choice != 0);

        scanner.close();
    }
}

class Book {
    private String title;
    private String author;
    private LibraryMember borrowedBy;

    public Book(String title, String author) {
        this.title = title;
        this.author = author;
        this.borrowedBy = null; // Initially, book is not borrowed
    }

    // Getters
    public String getTitle() {
        return title;
    }

    public String getAuthor() {
        return author;
    }

    public boolean isBorrowed() {
        return borrowedBy != null; // Book is considered borrowed if borrowedBy is not null
    }

    // Borrowing and returning methods
    public void borrowBook(LibraryMember member) {
        if (!isBorrowed()) {
            borrowedBy = member;
            System.out.println("Book '" + title + "' borrowed by member ID: " + member.getMemberId());
        } else {
            System.out.println("Book '" + title + "' is already borrowed by another member.");
        }
    }

    public void returnBook() {
        if (isBorrowed()) {
            borrowedBy = null;
            System.out.println("Book '" + title + "' returned.");
        } else {
            System.out.println("Book '" + title + "' was not borrowed.");
        }
    }
}

class LibraryMember {
    private String name;
    private int memberId;

    public LibraryMember(String name, int memberId) {
        this.name = name;
        this.memberId = memberId;
    }

    // Getters
    public String getName() {
        return name;
    }

    public int getMemberId() {
        return memberId;
    }
}

class Library {
    private Book[] books;
    private LibraryMember[] members;
    private int bookCount;
    private int memberCount;
    private Scanner scanner;

    public Library(int maxBooks, int maxMembers) {
        this.books = new Book[maxBooks];
        this.members = new LibraryMember[maxMembers];
        this.bookCount = 0;
        this.memberCount = 0;
        this.scanner = new Scanner(System.in);
    }

    public void addBook() {
        if (bookCount < books.length) {
            System.out.print("Enter book title: ");
            String title = scanner.nextLine();
            System.out.print("Enter book author: ");
            String author = scanner.nextLine();
            books[bookCount] = new Book(title, author);
            bookCount++;
            System.out.println("Book added to the library: " + title);
        } else {
            System.out.println("Cannot add more books. Library is full.");
        }
    }

    public void registerMember() {
        if (memberCount < members.length) {
            System.out.print("Enter member name: ");
            String name = scanner.nextLine();
            System.out.print("Enter member ID: ");
            int memberId = scanner.nextInt();
            scanner.nextLine(); // Consume newline character after nextInt()
            members[memberCount] = new LibraryMember(name, memberId);
            memberCount++;
            System.out.println("Member registered: " + name);
        } else {
            System.out.println("Cannot register more members. Library is full.");
        }
    }

    public void borrowBook() {
        System.out.print("Enter book title to borrow: ");
        String title = scanner.nextLine();
        System.out.print("Enter member ID: ");
        int memberId = scanner.nextInt();
        scanner.nextLine(); // Consume newline character after nextInt()

        boolean foundBook = false;
        for (int i = 0; i < bookCount; i++) {
            if (books[i].getTitle().equalsIgnoreCase(title)) {
                books[i].borrowBook(members[findMemberIndex(memberId)]);
                foundBook = true;
                break;
            }
        }
        if (!foundBook) {
            System.out.println("Book '" + title + "' is not available in the library.");
        }
    }

    public void returnBook() {
        System.out.print("Enter book title to return: ");
        String title = scanner.nextLine();
        System.out.print("Enter member ID: ");
        int memberId = scanner.nextInt();
        scanner.nextLine(); // Consume newline character after nextInt()

        boolean foundBook = false;
        for (int i = 0; i < bookCount; i++) {
            if (books[i].getTitle().equalsIgnoreCase(title)) {
                books[i].returnBook();
                foundBook = true;
                break;
            }
        }
        if (!foundBook) {
            System.out.println("Book '" + title + "' is not available in the library.");
        }
    }

    private int findMemberIndex(int memberId) {
        for (int i = 0; i < memberCount; i++) {
            if (members[i].getMemberId() == memberId) {
                return i;
            }
        }
        System.out.println("Member with ID " + memberId + " not found.");
        return -1;
    }
}
