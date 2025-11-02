import java.util.*;
class Library
{
    String books[];
    String Librarymember[];
    int bookCount;
    int memberCount;
    Book book;
    LibraryMember member;
    
    void setInfo()
    {
       Scanner sc=new Scanner(System.in);
       System.out.println("Enter number of books to be added");
       bookCount=sc.nextInt();
       System.out.println("Enter number of registered members");
       memberCount=sc.nextInt();
    }
    
    
        void Addbook()
        {
            String books[]=new String[bookCount];
            for(int count=0;count<=bookCount;count++)
            {
            book=new Book();
            book.setdata();
            if(count<bookCount)
            {
                System.out.println("Book has been added successfully");
                book.printdata();
            }
            else if(count==bookCount)
            {
                System.out.println("Max limit reached.Cant add");
            }
            }
        }   
            
            void registerMember()
            {
                String LibraryMember[]=new String[memberCount];
                for(int count=0;count<=memberCount;count++)
            {
            member=new LibraryMember();
            member.setData();
            if(count<memberCount)
            {
                System.out.println("Member has been added successfully");
                member.printData();
            }
            else if(count==bookCount)
            {
                System.out.println("Max limit reached.Cant add");
            }
            }
            }
            void borrowBook(String title,int memberid)
            {
                System.out.println("Title:"+title+"MemberID"+memberid+" has been borrowed successfully");
            }
            void returnBook(String title,int memberid)
            {
                System.out.println("Title:"+title+"MemberID"+memberid+" has been returned successfully");
            }
            
        

}
class Book 
{
    String title;
    String author;
    Boolean isBorrowed;
    void setdata()
    {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter title of book");
        title=sc.next();
        System.out.println("Enter the author of book");
        author=sc.next();
    }
    void printdata()
    {
        System.out.println("Title of book:"+title+"Author of book"+author);
    }
}
class LibraryMember
{
    String name;
    int memberid;
    void setData()
    {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the name of member");
        name=sc.next();
        System.out.println("Enter the id of the member");
        memberid=sc.nextInt();
    }
    void printData()
    {
        System.out.println("Name of registered member:"+name+". ID:"+memberid);
    }
}
public class Main
{
	public static void main(String[] args) {
	Scanner sc=new Scanner(System.in);
    Library lib=new Library();
    lib.setInfo();
    lib.Addbook();
    lib.registerMember();
    while(true)
    {
    System.out.println("Enter choice \n1.Borrow Book \n2.Return Book \n3.Exit");
    int choice=sc.nextInt();
    if(choice==1)
    {
        System.out.println("Enter the title of book");
        String t=sc.next();
        System.out.println("Enter memberID");
        int i=sc.nextInt();
        lib.borrowBook(t,i);
    }
    if(choice==2)
    {
        System.out.println("Enter the title of book");
        String t=sc.next();
        System.out.println("Enter memberID");
        int i=sc.nextInt();
        lib.returnBook(t,i);
    }
    else
    break;
	}
}
}