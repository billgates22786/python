import java.util.Scanner;
class ClassDetails 
{
    public static void main(String[] args) 
    {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter number of students: ");
        int n = input.nextInt();
        Student[] students = new Student[n];
        for (int i = 0; i < n; i++) 
        {
            students[i] = new Student(); 
            students[i].setInfo(); 
        }
        for (int i = 0; i < n - 1; i++)
        {
            for (int j = 0; j < n - i - 1; j++) 
            {
                if (students[j].totalMarks < students[j + 1].totalMarks) 
                {
                    Student temp = students[j];
                    students[j] = students[j + 1];
                    students[j + 1] = temp;
                }
            }
        }
        System.out.println("MERIT LIST: ");
        System.out.println("ID\tName\tCourse\tTotal Marks");
        for (int i = 0; i < n; i++) 
        {
            students[i].displayData();
        }
    }    
}
class Student 
{
    int id;
    String name;
    String course;
    int totalMarks;
    void setInfo() 
    {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the student ID: ");
        id = input.nextInt();
        System.out.print("Enter student name: ");
        name = input.next(); 
        System.out.print("Enter course: ");
        course = input.next();
        System.out.print("Enter total marks of the student: ");
        totalMarks = input.nextInt();
    }
    void displayData() 
    {
        System.out.println(id + "\t" + name + "\t" + course + "\t" + totalMarks);
    }
}
