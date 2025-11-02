import java.util.Scanner;
class Three
{
    public static void main(String[] args)
    {
        int a,b,c,d;
        Scanner in = new Scanner(System.in);
        System.out.print("ENTER THE FIRST NUMBER: ");
        a=in.nextInt();
        System.out.println("\u0007");
        System.out.print("ENTER THE SECOND NUMBER: ");
        b=in.nextInt();
        System.out.println("\u0007");
        System.out.print("ENTER THE THIRD NUMBER: ");
        c=in.nextInt();
        System.out.println("\u0007");
        d=a>b?a>c?a:c:b>c?b:c;
        System.out.println("ENTER THE GREATEST NUMBER: "+d);
        
    }
}