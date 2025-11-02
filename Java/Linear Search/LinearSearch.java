import java.util.Scanner;
class LinearSearch 
{
    public static void main(String[] args) 
    {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the number of elements: ");
        int n = input.nextInt();
        int a[] = new int[n]; 
        System.out.println("Enter the elements:");
        for (int i = 0; i < n; i++) 
        {
            System.out.print("Enter "+(i+1)+" element of index number "+(i)+" : ");
            a[i] = input.nextInt(); 
        }
        System.out.print("Enter an element to search: ");
        int element = input.nextInt();
        int index = linearSearch(a, element);
        if (index == -1)
            System.out.println("Element not found in the array");
        else
            System.out.println("Element found at index " + index);
    } 
    static int linearSearch(int[] a, int element) 
    {
        int position  = -1;
        int size = a.length;
        for (int i=0;i<size;i++) 
        {
            if (a[i]==element) 
            {
                position = i;
                break;
            }
        }
        return position;
    }
}
