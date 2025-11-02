import java.util.Scanner;
class Merge 
{
    public static void main(String[] args) 
    {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the number of names to be input: ");
        int num = input.nextInt();
        String firstNames [] = new String[num];
        String lastNames [] = new String[num]; 
        for(int i=0;i<num;i++) 
        {
            System.out.print("Enter First Name: ");
            firstNames[i] = input.next();
            System.out.print("Enter Last Name: ");
            lastNames[i] = input.next();
        }
        System.out.println("Names entered:");
        for(int i=0;i<num;i++) 
        {
            System.out.println(firstNames[i] + " " + lastNames[i]);
        }
    }
}
