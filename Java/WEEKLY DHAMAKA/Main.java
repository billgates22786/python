import java.util.Scanner;
class Student
{
    String name;
    int id;
    Scanner input = new Scanner(System.in);
    Student(String n,int i)
    {
        name = n;
        id = i;
    }
    // void inputData()
    // {
    //     System.out.println("Enter the name of the student: ");
    //     name = input.next();
    //     System.out.println("Enter id of the student: ");
    //     id = input.nextInt();
    // }
    void displayData()
    {
        System.out.println("NAME OF THE STUDENT: "+name);
        System.out.println("ID OF THE STUDENT: "+id);
    }
}
class 
class Main 
{
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter name of the student: ");
        String name = scanner.next();
        System.out.print("Enter id of the student: ");
        int id = scanner.nextInt();

        Student s = new Student(name, id);
        s.displayData();
    }
}