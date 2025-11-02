class Main 
{
    static int a = 10;
    static int b;      
    static
    {
        b = a * a;     
    }

    public static void main(String[] args) {
        System.out.println("Value of a : " + a);  
        System.out.println("Value of b : " + b); 
    }
}
