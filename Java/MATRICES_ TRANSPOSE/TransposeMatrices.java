import java.util.Scanner;
class TransposeMatrices 
{
    public static void main(String[] args) 
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of rows: ");
        int r = sc.nextInt();
        System.out.print("Enter the number of columns: ");
        int c = sc.nextInt();
        int a[][] = new int[r][c];
        System.out.println("Enter the matrix:");
        for (int i = 0; i < r; i++) 
        {
            for (int j = 0; j < c; j++) 
            {
                a[i][j] = sc.nextInt();
                System.out.print(a[i][j] + "\t");
            }
            System.out.println();
        }
        System.out.println("Actual matrix before Transpose:");
        for (int i = 0; i < c; i++) 
        {
            for (int j = 0; j < r; j++) 
            {
                System.out.print(a[i][j] + "\t");
            }
            System.out.println();
        }
        System.out.println("Transpose of the matrix:");
        for (int i = 0; i < c; i++) 
        {
            for (int j = 0; j < r; j++) 
            {
                System.out.print(a[j][i] + "\t");
            }
            System.out.println();
        }
    }
}
