class Book
{
	String title;
    String author;
    int yearPublished;
    String genre;
    String available;

}
class Main
{
    public static void main (String[] args) 
    {
        Book b1 = new Book();
        b1.title = "The Lord Of Rings";
        b1.author = "J.R.R.Tolkien";
        b1.yearPublished = 1954;
        b1.genre = "Fantasy";
        b1.available = "yes";
        System.out.println("BOOK 1");
        System.out.println(" TITLE:-  "+b1.title);
        System.out.println(" AUTHOR:- "+b1.author);
        System.out.println(" YEAR PUBLISHED:- "+b1.yearPublished);
        System.out.println(" GENRE:- "+b1.genre);
        System.out.println(" AVAILABLE:- "+b1.available);
        System.out.println("******************************************************");
        Book b2 = new Book();
        b2.title = "Rich Dad Poor Dad";
        b2.author = "Robert T. Kiyosaki";
        b2.yearPublished = 1997;
        b2.genre = "Self Help";
        b2.available = "yes";
        System.out.println("BOOK 2");
        System.out.println(" TITLE:-  "+b2.title);
        System.out.println(" AUTHOR:- "+b2.author);
        System.out.println(" YEAR PUBLISHED:- "+b2.yearPublished);
        System.out.println(" GENRE:- "+b2.genre);
        System.out.println(" AVAILABLE:- "+b2.available);
    }

}