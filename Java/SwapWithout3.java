public class SwapWithout3 {
    public static void main(String[] args) 
	{
		int x = 10;  // x is assigned the value 10
		int y = 15;  // y is assigned the value 15
		
		// Swap the values using a temporary variable
		int temp = x; // temp stores the value of x (10)
		x = y;        // x is now assigned the value of y (15)
		y = temp;     // y is now assigned the value of temp (10)

		System.out.println("Value of x =" + x); // x is now 15
		System.out.println("Value of y =" + y); // y is now 10
	}
}
