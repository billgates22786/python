class Swap
{
	public static void main(String[] args) 
	{
		int x = 10;
		int y = 15;
		x=y;
		y=x=y;
		System.out.println("Value of x ="+x);
		System.out.println("Value of y ="+y);
	}
}
