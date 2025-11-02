import java.util.Scanner;
class ExceptionEx3
{
	public static void main(String[] args) 
	{
	    Scanner input = new Scanner(System.in);
	    System.out.print("Enter number of elements in array: ");
	    int n = input.nextInt();
	    int arr[] = new int[n];
	    try 
	    {
	        System.out.println("Array = "+arr[n+1]);
	        System.out.println("After Exception ");
	    } catch(ArrayIndexOutOfBoundsException e)
	    {
	        System.out.println(e);
	        System.out.println(e.getMessage());
            System.out.println(e.getClass());
            System.out.println(e.getCause());
            e.printStackTrace();
	    }
	    int a = 25;
	    int b = 0;
	    int mul = a*b;
	    System.out.println("Multiply = "+mul);
	}
}
