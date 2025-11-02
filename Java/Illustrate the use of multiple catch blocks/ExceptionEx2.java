import java.util.Scanner;
class ExceptionEx2
{
	public static void main(String[] args) 
	{
	    Scanner input = new Scanner(System.in);
	    System.out.print("Enter the number of elements in array: ");
	    int n = input.nextInt();
	    int arr[] = new int[n];
	    int a=10;
	    int b=0;
	    try
	    {
	        int div = a/b;
	        System.out.println("DIVISION: "+div);
	        System.out.println("After division ");
	    }
	    catch(ArithmeticException e)
	    {
	        System.out.println(e);
	    }
	    try
	    {
	        System.out.println("Array = "+arr[n+1]);
	        System.out.println("After Exception ");
	    } 
	    catch(ArrayIndexOutOfBoundsException e)
	    {
	        System.out.println(e);
	    }
	}
}
