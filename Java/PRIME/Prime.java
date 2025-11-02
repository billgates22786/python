import java.util.Scanner;
class Prime 
{
    public static void main(String[] args) 
    {
        int p;
        Scanner input = new Scanner(System.in);
        System.out.print("ENTER THE NUMBER: ");
        p = input.nextInt();
        for (int i = 2; i * i <= p; i++) 
        { 
            if (p % i == 0)
            {
                 System.out.println(p + " is not a prime number.");
                
            }
            else
            {
                 System.out.println(p + " is a prime number."); 
                
            
            }
        }
    }
}
