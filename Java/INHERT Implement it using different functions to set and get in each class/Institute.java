class Institute
{
    public static void main(String[] args)
    {
       Student s = new Student();
       Teacher t = new Teacher();
       
       s.setData("Kartikay","7658800579","kartikayjain123@gmail.com","BCA");
       s.mountData("Male","2736 Jain Street Near Jain Mandir,Nakodar");
       t.getData("ab+","excellent");
       s.printData();
       s.fixData();
       t.settleData();
    }
}
class Person 
{
    String name;
    String contact;
    String emailId;
    String course;
    
    void setData(String n,String c,String e,String co)
    {
        name = n;
        contact = c;
        emailId = e;
        course = co;
    }
    
    void printData()
    {
        System.out.println("Person Detail");
        System.out.println("Name: "+name+'\n'+"Contact: "+contact+'\n'+"Email Id: "+emailId+'\n'+"Course: "+course);
    }
}
class Student extends Person
{
    String gender;
    String address;
    void mountData(String g,String a)
    {
       gender = g;
       address = a;
    }
    void fixData()
    {
        System.out.println("Student Detail");
        System.out.println("Gender: "+gender+'\n'+"Address: "+address);
    }
}
class Teacher extends Person 
{
    String bloodGroup;
    String performance;
    void getData(String b,String p)
    {
        bloodGroup = b;
        performance = p;
    }
    void settleData()
    {
        System.out.println("Teacher Detail");
        System.out.println("Blood Group: "+bloodGroup+'\n'+"Performance: "+performance);
    }
}

