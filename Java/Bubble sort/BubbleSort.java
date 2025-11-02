import java.util.Scanner;
class BubbleSort {

   public static void main(String [] ar)
   {
    Scanner input = new Scanner(System.in);
    System.out.print("Enter number of the elements in the array: ");
    int n = input.nextInt();
    int a[]= new int [n] ;
    int element;
    System.out.println("Enter an unsorted array ");
    for(int i=0;i<5;i++)
    {
        System.out.print("Enter "+(i+1)+" element of index number "+(i)+" : ");
        a[i]= input.nextInt();
    }  
     int [] sortedArray = bubbleSort(a); 
     System.out.println("Sorted array is");
     for(int i=0;i<5;i++)
        {
            System.out.println("Element "+(i+1)+" after sorting is: "+a[i]);
        }  
               
   }
   static int[] bubbleSort(int [] a)
   {
   
    int n=a.length;
    for(int i=0;i<n-1;i++)
    {
      for(int j=0;j<n-i-1;j++)
      {
        if(a[j]>a[j+1])
        {
            int temp = a[j];
            a[j]=a[j+1];
            a[j+1]=temp;
        }

      }
    }  

    return a;
   }
     


}