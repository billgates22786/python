class InterfacesEx
{
    public static void main(String[] args )
    {
        Person p = new Student();
        p.info();     
        p = new Teacher();
        p.info();
    }
}
interface Person  
{
   abstract void info();
  
}
class Student implements Person
{

   public void info()
    {
        System.out.println("Student Information");
    }
}
 class Teacher implements Person
{
   public void info()
    {
        System.out.println("Teacher Information");
    }
}