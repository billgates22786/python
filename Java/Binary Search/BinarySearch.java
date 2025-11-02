import java.util.Scanner;
class BinarySearch 
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
        int index = binarySearch(a, element);
        if (index == -1)
            System.out.println("Element not found in the array");
        else
            System.out.println("Element found at index " + index);
    } 

    static int binarySearch(int[] a, int element) 
    {
        int left = 0;
        int right = a.length - 1;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (a[mid] == element)
                return mid;
            if (a[mid] < element)
                left = mid + 1;
            else
                right = mid - 1;
        }
        return -1;
    }
}
