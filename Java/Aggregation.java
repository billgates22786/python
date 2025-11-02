import java.util.Scanner;
class Aggregation 
{
     public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter Number Of Students: ");
        int n = scanner.nextInt();
        for(int i=1; i<=n;i++)
       {
        System.out.print("Enter student ID: ");
        int id = scanner.nextInt();
        scanner.nextLine(); 
        System.out.print("Enter student name: ");
        String name = scanner.nextLine();
        Student s = new Student(id, name);
        System.out.print("Enter city name: ");
        String city = scanner.nextLine();
        System.out.print("Enter state name: ");
        String state = scanner.nextLine();
        System.out.print("Enter country name: ");
        String country = scanner.nextLine();
        Address a = new Address(city, state, country);
        System.out.print("Enter day of birth: ");
        int day = scanner.nextInt();
        System.out.print("Enter month of birth: ");
        int month = scanner.nextInt();
        System.out.print("Enter year of birth: ");
        int year = scanner.nextInt();
        Dob d = new Dob(day, month, year);
        s.display();
        a.printData();
        d.pasteData();
       }
        
    }
}
class Student 
{
    int id;
    String name;
    Address address;
    Dob dob;
    Student(int i,String n)
    {
        id = i;
        name = n;
    }
    void display()
    {
        System.out.println("Student Id: "+id+'\n'+"Student Name: "+name);
    }
}
class Address
{
    String city;
    String state;
    String country;
    Address(String c,String s,String ct)
    {
        city = c;
        state = s;
        country = ct;
    }
    void printData()
    {
        System.out.println("City Name: "+city+'\n'+"State Name: "+state+'\n'+"Country Name: "+country);
    }
}
class Dob
{
    int day;
    int month;
    int year;
    Dob(int d,int m,int y)
    {
        day = d;
        month = m;
        year = y;
    }
    void pasteData()
    {
        System.out.println("Day Of Birth: "+day+"-"+month+"-"+year);
    }
}
 