class OverloadingExample 
{
    public static void main(String[] args)
    {
       System.out.print("AREA OF RECTANGLE:- ");
       multiply(4,5);
       System.out.print("AREA OF SQUARE:- ");
       multiply(4);
       System.out.print("AREA OF CUBOID:- ");
       multiply(8,5,6);
      
    }
    static int multiply(int x,int y)
    {
        System.out.println(x*y);
        return (x*y);
    }
    static int multiply(int x)
    {
        System.out.println(x*x);
        return (x*x);
    }
    static int multiply(int x,int y,int z)
    {
        System.out.println(x*y*z);
        return (x*y*z);
    }
    
}