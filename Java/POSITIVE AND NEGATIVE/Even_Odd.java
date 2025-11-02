import java.util.Scanner;
class Even_Odd
{
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int number;
		System.out.print("ENTER THE NUMBER :");
		number = in.nextInt();
		if(number<0)
		{
		    System.out.println("THE NUMBER IS OF NEGATIVE NATURE");
		}
		else
		{
		    System.out.println("THE NUMBER IS OF POSITIVE NATURE");
		}
		
	}
}
