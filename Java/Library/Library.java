
import java.util.Scanner;
class Library
{
	public static void main(String[] args) 
	{
	    Scanner input = new Scanner(System.in);
        LibraryMember[] member = new LibraryMember[100];
        Books[] books = new Books[100];
	    Books b = new Books();
        b.set();
	}
}
class Books extends Library
{
    String title;
    String author;
    int isBorrowed = 0 ;
    int bookCount;

    Books(String t, String a,int i,int b)
    {
        title = t;
        author = a;
        isBorrowed = i;
        bookCount = b;
    }
	Scanner input = new Scanner(System.in);
    void add()
    {
        System.out.println("Enter the capacity of books in the library: ");
	    int n = input.nextInt();
	    
        for(int i=0;i<n;i++)
        {
        System.out.print("Enter book name: ");
        title = input.next();
        System.out.print("Enter author name:");
        author = input.next();
        }
    }
    void set()
    {
        System.out.println("Title \t\t"+title+"Author \t\t"+author);
    }

    void borrowBook()
    {  
        System.out.println("Book Borrowed by");
    }
    void returnBook()
    {
        System.out.println("Book Return :");
        
    }
}
class LibraryMember extends Library
{
    Scanner input = new Scanner(System.in);
    int memberId;
    String name;
    int memberCount;
    LibraryMember(int m,String n,int mc)
    {
        memberId = m;
        name = n;
        memberCount = mc;
    }
    void setMember()
    {
        System.out.print("Enter the number of library member in the library: ");
        int k = input.nextInt();
        for(int i=0;i<k;i++)
        {
            System.out.print("Enter memberId: ");
            memberId = input.nextInt();
            System.out.print("Enter name: ");
            name = input.next();
        }

    }
    
}


