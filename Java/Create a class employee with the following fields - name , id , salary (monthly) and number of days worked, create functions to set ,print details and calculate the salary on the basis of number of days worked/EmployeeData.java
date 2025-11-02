class Office
{
    String name;
    int officeId;
    int salary;
    int daysWorked;
    
    public void officeData(String n,int o,int s,int d)
    {
        name = n;
        officeId = o;
        salary = s;
        daysWorked = d;
    }
    public void printOfficeData()
    {
        System.out.println("NAME OF THE EMPLOYEE: "+name);
        System.out.println("OFFICE ID OF THE EMPLOYEE: "+officeId);
        System.out.println("PER DAY SALARY OF THE EMPLOYEE: "+salary);
        System.out.println("NUMBER OF DAYS EMPLOYEE WORKED: "+daysWorked);
    }
    public int salaryCalculate()
    {
       System.out.print("TOTAL SALARY OF THE EMPLOYEE "+name+" IS: " );
       return(salary*daysWorked);
    }
    public void space()
    {
        System.out.println('\n'+"*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*");
    }
    
}
class EmployeeData
{
    public static void main(String[] args)
    {
        Office o1 = new Office();
        o1.officeData("Kartikay",004,100,25);
        o1.printOfficeData();
        System.out.print(o1.salaryCalculate());
        o1.space();
        Office o2 = new Office();
        o2.officeData("Stuti",005,150,28);
        o2.printOfficeData();
        System.out.println(o2.salaryCalculate());
       
        
    }
}