class Institute 
{
    public static void main(String[] args) 
    {
       Student s = new Student("Kartikay", "7658800579", "kartikayjain123@gmail.com", "BCA", "Male", "2736 Jain Street Near Jain Mandir, Nakodar");
       Teacher t = new Teacher("ab+", "excellent");
       s.printData();
       t.settleData();
    }
}

class Person 
{
    private String name;
    private String contact;
    private String emailId;
    private String course;

    Person(String n, String c, String e, String co) 
    {
        name = n;
        contact = c;
        emailId = e;
        course = co;
    }

    void printData() 
    {
        System.out.println("Person Detail");
        System.out.println("Name: " + name + '\n' + "Contact: " + contact + '\n' + "Email Id: " + emailId + '\n' + "Course: " + course);
    }
}

class Student extends Person {
    private String gender;
    private String address;
    Student(String n, String c, String e, String co, String g, String a) {
       super(n, c, e, co);
       gender = g;
       address = a;
    }
    void printData() 
    {
        super.printData();
        System.out.println("Student Detail");
        System.out.println("Gender: " + gender + '\n' + "Address: " + address);
    }
}

class Teacher extends Person {
    private String bloodGroup;
    private String performance;
    Teacher(String b, String p) {
        super("", "", "", ""); // Call to super constructor is necessary
        bloodGroup = b;
        performance = p;
    }
    void settleData() {
        System.out.println("Teacher Detail");
        System.out.println("Blood Group: " + bloodGroup + '\n' + "Performance: " + performance);
    }
}
