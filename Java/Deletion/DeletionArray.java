import java.util.Scanner;
class DeletionArray
{
    public static void main(String[] args)
    {
        int num,position,i;
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the number of elements: ");
        num = input.nextInt();
        int[] arr = new int[num];
        System.out.println("Elements of the array are as follows: ");
        for(i=0;i<num;i++)
        {
            System.out.print("Input "+(i+1)+" Element: ");
            arr[i] = input.nextInt();
        }
        System.out.println("Enter the position to delete: ");
        position = input.nextInt();
        if(position<num)
        {
            for(i=position;i<num-1;i++)
            {
            arr[i]=arr[i+1];
                
            }
        }
        else
        {
            System.out.println("Invalid Input");
        }
        num=num-1;
        for(i=0;i<num;i++)
        {
            System.out.println((i+1)+" Elements after updation: "+arr[i]);
        }
    }
}