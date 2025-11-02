import java.util.Scanner;
class DiagonalMatrices
{
    public static void main(String[] args)
    {
        int r,c;
        Scanner input = new Scanner(System.in);
        System.out.print("ENTER THE NUMBER OF ROWS: ");
        r = input.nextInt();  // r= rows
        System.out.print("ENTER THE NUMBER OF COLUMNS: ");
        c = input.nextInt(); //c= COLUMNS
        int a [][] = new int[r][c];
        System.out.println("ENTER MATRIX:");
        for (int i=0; i<r; i++)
        {
            for(int j=0; j<c; j++)
            {
                a[i][j] = input.nextInt();
            }
        }
        
        int sumOfDiagonal = 0;
        for(int i =0;i<r;i++)
        {
            for(int j=0;j<c;j++)
            {
                if(i==j)
                {
                    sumOfDiagonal += a[i][j];
                }
            }
        }
        System.out.println("Sum of the diagonal elements: " + sumOfDiagonal);

    }
}