class Main
{
	public static void main(String[] args) {
		Distance d1 = new Distance(100,4000,5089);
		Distance d2 = new Distance(152,2000,40520);
		d1.display();
		d2.display();
		Distance d3 = d1.add(d2);
		d3.display();
	}
}
class Distance
{
    int k;
    int m;
    int c;
    
    Distance()
    {
        
    }
    Distance(int k,int m,int c)
    {
        this.k = k;
        this.m = m;
        this.c = c;
    }
    void display()
    {
        System.out.println(k+"."+m+"."+c);
    }
    
    Distance add(Distance d)
    {
        Distance temp = new Distance();
        temp.k= k+d.k;
        temp.m= m+d.m;
        temp.c= c+d.c;
        if(temp.c >= 100)
        {
     
            temp.m +=(temp.c/100);
           temp.c= (temp.c %100);
        }
        if(temp.m >= 1000)
        {
       
            temp.k +=(temp.m/1000);
            temp.m= (temp.m %1000);
        }
        return temp;
    }
}
