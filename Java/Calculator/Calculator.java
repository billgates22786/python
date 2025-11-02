import java.util.Scanner;
class Calculator 
{
    public static void main(String[] args) 
    {
        Scanner input = new Scanner(System.in);
        float a, b; 
        
        float operator;
        do
        {
            System.out.print("Enter the first number: ");
            a = input.nextFloat(); 
            System.out.print("Enter the second number: ");
            b = input.nextFloat();
            System.out.println("Choose an operation:");
            System.out.println("1. Addition");
            System.out.println("2. Subtraction");
            System.out.println("3. Multiplication");
            System.out.println("4. Division");
            System.out.println("5. Modulus");
            System.out.println("6. Exit");
            System.out.print("ENTER THE OPERATOR:- ");
            operator = input.nextFloat();
        if(operator==1)
        {
            float sum = a+b;
            System.out.println("SUM OF THE NUMBERS:- "+sum);
        }
        else if(operator==2)
        {
            float sub = a-b;
            System.out.println("SUB OF THE NUMBERS:- "+sub);
        }
        else if(operator==3)
        {
            float multi = a*b;
            System.out.println("MULTIPLICATION OF THE NUMBERS:- "+multi);
        }
        else if(operator==4)
        {
            float divi = a/b;
            System.out.println("DIVISION OF THE NUMBERS:- "+divi);
        }
        else if(operator==5)
        {
            float mod =a%b;
            System.out.println("MODULUS OF THE NUMBERS:- "+mod);
        }
        else if(operator==6)
        {
            System.out.println("GOODBYE");
        }
        }while (operator != 6);
        
    }
}
