class Interface 
{
  public static void main (String[]args)
  {
	Shape s = new Rectangle();
	s.display();
	s = new Square();
	s.display();
  }
}
interface Shape
{
    
  abstract void display();
}
class Rectangle implements Shape
{
   public void display()
  {
	System.out.println ("AREA OF THE RECTANGLE ");
  }
}
class Square implements Shape
{
    public void display()
    {
        System.out.println("AREA OF THE SQUARE ");
    }

}
