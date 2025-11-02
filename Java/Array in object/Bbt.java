import java.util.Scanner;
class Bbt
// full form of bbt is big boyz toy 
{
	public static void main(String[] args) 
	{
	    Scanner sc = new Scanner(System.in);
	    System.out.print("Enter The Number Of Priceless Possession: ");
	    int n = sc.nextInt();
	    Showroom[] Showroom = new Showroom[n];
	    for(int i=0;i<n;i++)
	    {
	        Showroom[i] = new Showroom();
	        System.out.println("Enter the car details: "+(i+1));
	        Showroom[i].inputData();
	    }
	    System.out.println("CAR DETAILS: ");
	    System.out.println("*****************************************************************************************");
	    System.out.println("CarType\t\t\tEngine\t\t\tColour\t\t\tPrice");
	    for(int i=0;i<n;i++)
	    {
	        
	       // System.out.println("Car Details For "+(i+1));
	        Showroom[i].printData();
	    }
	}
}
class Showroom
{
    String carType;
    String engine;
    String colour;
    String price;
    
    void inputData()
    {
        Scanner input = new Scanner(System.in);
        System.out.print("Car type: ");
        carType = input.next();
        System.out.print("Engine: ");
        engine = input.next();
        System.out.print("Colour: ");
        colour = input.next();
        System.out.print("Price: ");
        price = input.next();
    }
    void printData()
    {
        // System.out.println("Car Type "+carType);
        // System.out.println("Engine "+engine);
        // System.out.println("Colour "+colour);
        // System.out.println("Price "+price);
        System.out.println(carType+"\t\t\t"+engine+"\t\t\t"+colour+"\t\t\t"+price);
    }
    //TO GET PERFECT OUTPUT PLEASE INPUT THE BELOW GIVEN DATA
    //Enter first car type = BMW 
    //Enter first car engine = S50
    //Enter first car colour = black
    //Enter first car price = 1,00,00,000
    
    
    //Enter second car type = BMW 
    //Enter second car engine = S62
    //Enter second car colour = orange
    //Enter second car price = 1,74,00,000
}
