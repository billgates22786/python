import java.util.Scanner;
class Fibonacci 
{
    public static void fibonacci(int n) 
    {
        int a = 0, b = 1, c;
        System.out.println("FIBONACCI SERIES");

        for (int i = 0; i < n; i++) 
        {
            System.out.print(a + "\t");  
            c = a + b;
            a = b;
            b = c;
        }
    }
    public static void main(String[] args) 
    {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the number of terms: ");
        int n = input.nextInt();
        fibonacci(n);
    }
}
