class Main
{
	public static void main(String[] args) 
	{
	    Area a = new Area();
	    a.setData(7);
	    a.display();
	
	}
}
class Area
{
    double radius;
    final double pie = 3.14;
    void setData(double r)
    {
        radius = r;
    }
    void display()
    {
        System.out.println("Area of the circle: "+(pie*radius*radius));
    }
}