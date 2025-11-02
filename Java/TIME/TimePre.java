import java.util.Scanner;
class TimePre {
    public static void main(String[] args) 
    {
        Scanner input = new Scanner(System.in);
        Time t1 = new Time();
        System.out.print("ENTER HOURS (1):");
        t1.h= input.nextInt();
        System.out.print("ENTER MINUTES (1):");
        t1.m= input.nextInt();
        System.out.print("ENTER SECONDS (1):");
        t1.s= input.nextInt();
        Time t2= new Time();
        System.out.print("ENTER HOURS (2):");
        t2.h= input.nextInt();
        System.out.print("ENTER MINUTES (2):");
        t2.m= input.nextInt();
        System.out.print("ENTER SECONDS (2):");
        t2.s= input.nextInt();
        t1.display();
        t2.display();
        Time t3 = t1.add(t2);
        t3.display();
    }
}
class Time{
    int h;
    int m;
    int s;
    Time()
    {
        
    }
    Time(int h,int m)
    {
        this.h= h;
        this.m= m;
      
    }
    Time(int h,int m, int s)
    {
        this(h,m);
        this.s= s;
    }
    void display()
    {
        System.out.println(h+":"+m+":"+s);
    }
    Time add(Time t)
    {
        Time temp = new Time();
        temp.h= h+t.h;
        temp.m= m+t.m;
        temp.s= s+t.s;
        
        if(temp.s >= 60)
        {
     
            temp.m +=(temp.s/60);
           temp.s= (temp.s %60);
        }
        if(temp.m >= 60)
        {
       
            temp.h +=(temp.m/60);
            temp.m= (temp.m %60);
        }
        return temp;
    }
    
    
}