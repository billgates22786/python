public class PrefixAndPostfix {
    public static void main(String[] args) 
	{
	    int a=25,b,c=25,d;
	    b=a++;
	    d=++c;
	    System.out.println("POSTFIX INCREMENT");
		System.out.println("VALUE OF A = "+a);
		System.out.println("VALUE OF B = "+b);
		System.out.println("PREFIX INCREMENT");
		System.out.println("VALUE OF C = "+c);
		System.out.println("VALUE OF D = "+d);
	}
}
