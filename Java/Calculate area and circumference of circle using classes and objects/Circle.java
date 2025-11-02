import java.util.Scanner;
class Circle 
{
    public static void main(String args[])
    {
        Scanner input = new Scanner(System.in);
        System.out.print("ENTER THE VALUE OF RADIUS = ");
        int k = input.nextInt();
        CircleAreaCircumference c1 = new CircleAreaCircumference();
        CircleAreaCircumference c2 = new CircleAreaCircumference(k);
        //   c1.area();
        c2.area();
        c2.circumference();
    }
}
class CircleAreaCircumference
{
    private float r;
    
    CircleAreaCircumference()
    {
       r=1; 
    }
    CircleAreaCircumference(int x)
    {
        r=x;
    }
    void area()
    {
        System.out.println("AREA OF THE CIRCLE = "+(22*r*r/7));
    }
    void circumference()
    {
        System.out.println("CIRCUMFERENCE OF THE CIRCLE = "+(2*22*r/7));
    }
}