class Main
{
	public static void main(String[] args) 
	{
		Electricity b1 = new Electricity(100,"Kartikay",500);
		b1.printData();
		Electricity b2 = new Electricity(101,"Scooty",5000);
		b1.printData();
	}
}
class Electricity
{
    private int id;
    private String name;
    private int unit;
    public Electricity(int i,String n,int u)
    {
        id = i;
        name = n;
        unit = u;
    }
    public void printData()
    {
        System.out.println("ID OF THE CUSTOMER: "+id);
        System.out.println("NAME OF THE CUSTOMER: "+name);
        System.out.println("UNIT CONSUMED: "+unit);
        if(unit<=600)
        {
            System.out.println("AUTOMATED BILL GENERATED = 0");
        }
        else
        {
            int bill = unit*8;
            System.out.println("BILL OF THE CUSTOMER = "+bill);
        }
    }
}
