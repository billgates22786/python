import java.util.Scanner;
class Matrices
{
    public static void main(String[] args) 
    {
        Scanner input = new Scanner(System.in);
        System.out.print("ENTER THE NUMBER OF ROWS: ");
        int r = input.nextInt();
        System.out.print("ENTER THE NUMBER OF COLUMNS: ");
        int c = input.nextInt();
        int a[][] = new int[r][c];
        System.out.println("ENTER MATRIX 1: ");
        for (int i = 0; i < r; i++) 
        {
            for (int j = 0; j < c; j++) 
            {
                a[i][j] = input.nextInt();
                System.out.print(a[i][j] + "\t");
            }
            System.out.println();
        }
        int b[][] = new int[r][c];
        System.out.println("ENTER MATRIX 2: ");
        for (int i = 0; i < r; i++) 
        {
            for (int j = 0; j < c; j++) 
            {
                b[i][j] = input.nextInt();
                System.out.print(b[i][j] + "\t");
            }
            System.out.println();
        }
        int sum[][] = new int[r][c];
        for (int i = 0; i < r; i++) 
        {
            for (int j = 0; j < c; j++) 
            {
                sum[i][j] = a[i][j] + b[i][j];
            }
        }
        System.out.println("SUM OF MATRICES: ");
        for (int i = 0; i < r; i++) 
        {
            for (int j = 0; j < c; j++) 
            {
                System.out.print(sum[i][j] + "\t");
            }
            System.out.println();
        }
        
    }
}
