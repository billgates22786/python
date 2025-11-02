class Main
{
  public static void main (String[]args)
  {
	Shape s = new Rectangle();
	s.setData(4,4);
	s.display();
	s = new Square();
	s.setData(4,5);
	s.display();
  }
}
class Shape
{
    int l,b;
    void setData(int a,int c){
        l = a;
        b = c;
    }
  void display ()
  {
	System.out.println ("AREA OF THE  ");
  }
}
class Rectangle extends Shape
{
  void display ()
  {
	System.out.println ("AREA OF THE RECTANGLE "+(l*l));
  }
}
class Square extends Shape
{
void display()
    {
        System.out.println("AREA OF THE SQUARE "+(l*b));
    }

}
