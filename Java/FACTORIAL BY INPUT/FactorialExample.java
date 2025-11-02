import java.util.Scanner;

class FactorialExample
{
    public static void main(String[] args) 
    {
        int n;
        Scanner input = new Scanner(System.in);
        System.out.print("ENTER THE NUMBER:- ");
        n = input.nextInt();
        int result = fact(n);
        System.out.println("The factorial of " + n + " is: " + result);
    }
    static int fact(int n) 
    {
        if (n == 0) 
        { 
            return 1;
        } else 
        {
            return n * fact(n - 1);
        }
    }
}
