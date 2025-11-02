import java.util.Scanner;
class InsertInArrayEnd
{
	public static void main(String[] args) 
	{
	    int n,i,k,element;
	    Scanner input = new Scanner(System.in);
	    System.out.print("Enter the number of element: ");
	    n = input.nextInt();
	    int array[] = new int[n+1];
	    System.out.println("Enter The Element: ");
	    for(i=0;i<n;i++)
	    {
	        System.out.print("Enter "+(i+1)+" element: ");
	        array[i] = input.nextInt();
	    }
	    k = n;
	    System.out.print("Enter the element to add at the last: ");
	    element = input.nextInt();
	    for(i=n-1;i>=k;i--)
	    {
	        array[i+1] = array[i];
	    }
	    System.out.println("Enter the new array list: ");
	    array[k] = element;
	    n=n+1;
	    for(i=0;i<n;i++)
	    {
	        System.out.print("Element "+(i+1)+" element: ");
	        System.out.println(array[i]);
	    }
	    
	}
}