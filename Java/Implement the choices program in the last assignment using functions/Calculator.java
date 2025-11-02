import java.util.Scanner;

class Calculator 
{
    
    static void add(float a, float b) 
    {
        float sum = a + b;
        System.out.println("SUM OF THE NUMBERS: " + sum);
    }
    
    static void subtract(float a, float b) 
    {
        float sub = a - b;
        System.out.println("SUBTRACTION OF THE NUMBERS: " + sub);
    }
    
    static void multiply(float a, float b) 
    {
        float multi = a * b;
        System.out.println("MULTIPLICATION OF THE NUMBERS: " + multi);
    }
    
    static void divide(float a, float b) 
    {
        float divi = a / b;
        System.out.println("DIVISION OF THE NUMBERS: " + divi);
    }
    
    static void modulus(float a, float b) 
    {
        float mod = a % b;
        System.out.println("MODULUS OF THE NUMBERS: " + mod);
    }
    
    public static void main(String[] args) 
    {
        Scanner input = new Scanner(System.in);
        float a, b;
        int operator;
        
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
            System.out.print("ENTER THE OPERATOR: ");
            operator = input.nextInt();
            
            switch (operator)
            {
                case 1:
                    add(a, b);
                    break;
                case 2:
                    subtract(a, b);
                    break;
                case 3:
                    multiply(a, b);
                    break;
                case 4:
                    divide(a, b);
                    break;
                case 5:
                    modulus(a, b);
                    break;
                case 6:
                    System.out.println("GOODBYE");
                    break;
                
            }
            
        } while (operator != 6);
    }
}
