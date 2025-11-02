import java.util.Scanner;
class Array  
{
	public static void main(String[] args) 
	{
	    int marks[];
	    int i,n;
	    Scanner input = new Scanner(System.in);
	    System.out.print("ENTER THE NUMBER: ");
	    n = input.nextInt();
	    marks = new int[n];
	    for(i=0;i<n;i++)
	    {
	        System.out.print("Enter the elements: ");
	        marks[i]= input.nextInt();
	    }
	    System.out.println("Subject Marks : ");
	    for(i=0;i<n;i++)
	    {
	        System.out.println("Marks In The Subject is : "+marks[i]);
	    }
	    int sum=0;
	    for(i=0;i<n;i++)
	    {
	         sum += marks[i];
	    }
	    int average = sum/n;
	    int highest = marks[0];
        for (i=1;i<n;i++) 
        {
            if (marks[i] > highest) 
            {
                highest = marks[i];
            }
        }
	    System.out.println("Total Marks: "+sum);
	    System.out.println("Average Marks: "+average);
	    System.out.println("Highest Marks: "+highest);
	    
	}
}