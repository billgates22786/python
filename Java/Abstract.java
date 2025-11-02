class Abstract 
{
  public static void main (String[]args)
  {
	Shape s = new Rectangle();
	s.display();
	s = new Square();
	s.display();
  }
}
abstract class Shape
{
    
  abstract void display();
}
class Rectangle extends Shape
{
  void display()
  {
	System.out.println ("AREA OF THE RECTANGLE ");
  }
}
class Square extends Shape
{
void display()
    {
        System.out.println("AREA OF THE SQUARE ");
    }

}
