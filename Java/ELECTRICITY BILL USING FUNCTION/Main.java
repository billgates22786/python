class Main 
{
    public static void main(String[] args)
    {
        Electricity b1 = new Electricity();
        b1.setData(100,"Kartikay",500);
        b1.PrintData();
        Electricity b2 = new Electricity();
        b2.setData(101,"Gaurav",5000);
        b2.PrintData();
        
    }
}
class Electricity
{
    private int id;
    private String name;
    private int unit;
    public void setData(int i,String n,int u)
    {
        id=i;
        name=n;
        unit=u;
        
    }
    public void PrintData()
    {
        System.out.println("ID OF THE CUSTOMER: "+id);
        System.out.println("NAME OF THE CUSTOMER: "+name);
        System.out.println("UNIT CONSUMED: "+unit);
        if(unit<=600)
        {
            System.out.println("AUTOMATED BILL GENERATED = 0");
        }
        else{
            int t=unit*8;
            System.out.println("BILL OF THE CUSTOMER = "+t);
        }
    }
}

