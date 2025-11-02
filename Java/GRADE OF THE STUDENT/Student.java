import java.util.Scanner;
class Student 
{
    public static void main(String[] args) 
    {
        int maths, chemistry, physics;
        System.out.println("ENTER THE MARKS OF THE STUDENT ");
        Scanner input = new Scanner(System.in);
        
        System.out.print("MARKS OF MATHS: ");
        maths = input.nextInt();
        if (maths > 100) 
        {
            System.out.println("Invalid input. Maths marks cannot exceed 100. Setting to 100.");
            maths = 100;
        }
        System.out.print("MARKS OF CHEMISTRY: ");
        chemistry = input.nextInt();
        if (chemistry > 100) 
        {
            System.out.println("Invalid input. Chemistry marks cannot exceed 100. Setting to 100.");
            chemistry = 100;
        }
        System.out.print("MARKS OF PHYSICS: ");
        physics = input.nextInt();
        if (physics > 100) 
        {
            System.out.println("Invalid input. Physics marks cannot exceed 100. Setting to 100.");
            physics = 100;
        }
        int total_marks = maths + chemistry + physics;
        int average = total_marks / 3;
        int percentage = (total_marks * 100) / 300; 
        System.out.println("TOTAL MARKS = " + total_marks);
        System.out.println("AVERAGE = " + average);
        System.out.println("Percentage = " + percentage + "%");
        if(percentage<100&&percentage>90)
        {
            System.out.println("GRADE OF THE STUDENT IS A+");
        }
        else if(percentage<90&&percentage>=80)
        {
            System.out.println("GRADE OF THE STUDENT IS A");
        }
        else if(percentage<80&&percentage>=70)
        {
            System.out.println("GRADE OF THE STUDENT IS B+");
        }
        else if(percentage<70&&percentage>=60)
        {
            System.out.println("GRADE OF THE STUDENT IS B");
        }
        else if(percentage<60&&percentage>50)
        {
            System.out.println("GRADE OF THE STUDENT IS C");
        }
        else if(percentage<=50)
        {
            System.out.println("FAIL FAIL FAIL ");
        }
    }
}
