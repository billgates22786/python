class MultipleInheritance
{
    public static void main(String[] a)
    {
        Bangan b = new Bangan();
        b.display();
    }
}
class Scooty   
{
    void display()
    {
        System.out.println("A class display method");
    }
}
interface Marazo
{
    abstract void display();
}
class Bangan extends Scooty implements Marazo 
{
    public void display()
    {
        System.out.println("Multiple Inheritance");
    }
}
