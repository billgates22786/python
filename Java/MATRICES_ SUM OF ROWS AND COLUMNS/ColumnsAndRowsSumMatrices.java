import java.util.Scanner;
class ColumnsAndRowsSumMatrices 
{
    public static void main(String[] args) 
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of rows: ");
        int r = sc.nextInt();
        System.out.print("Enter the number of columns: ");
        int c = sc.nextInt();
        int a[][] = new int[r][c];
        int col[] = new int[c];
        int row[]= new int[r];
        System.out.println("Enter Matrix :");
        for (int i = 0; i < r; i++) 
        {
            for (int j = 0; j < c; j++) 
            {
                a[i][j] = sc.nextInt();
                System.out.print(a[i][j] + "\t");
            }
            System.out.println();
        }
        for (int j = 0; j < c; j++) 
        {
            int sumOfColumns = 0; 
            for (int i = 0; i < r; i++) 
            {
                sumOfColumns += a[i][j];
            }
            col[j] = sumOfColumns; 
        }
        for(int i = 0;i<r;i++)
        {
            int sumOfRows=0;
            for(int j=0;j<c;j++)
            {
                sumOfRows+=a[i][j];
            }
            row[i]= sumOfRows;
        }

        System.out.println("print the column sum:");
        for (int j = 0; j < c; j++) 
        {
            System.out.println(col[j] + "\t");
        }
        System.out.println("print the rows sum:");
        for(int i=0;i<r;i++)
        {
            System.out.println(row[i]+"\t");
        }
    }
}
