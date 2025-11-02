import java.util.Scanner;
class AddAllNum
{
	public static void main(String[] args) 
	{
		int number;
		Scanner input = new Scanner(System.in);
		System.out.print("ENTER THE FOUR DIGIT NUMBER:- ");
		number = input.nextInt();
		int sum = 0;
		// Loop to add all digits 
		for(int i=0;i<4;i++)
		{
		    sum += number % 10; // To find the last digit and add it 
		    number /= 10; // Remove the last digit
		}
		
		System.out.println("The sum of the digits is: " + sum);
	}
}
