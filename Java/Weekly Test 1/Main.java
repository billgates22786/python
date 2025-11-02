class Main 
{
    public static void main(String[] args) 
    {
        Electronics e1 = new Electronics();
        Electronics e2 = new Electronics();
        e1.showcase("Dell", 50000);
        e1.displayData("2 years");
        e1.calculateFinalPrice();
        e1.printData();
        e1.printInfo();
        e2.showcase("Iphone", 150000);
        e2.displayData("1 years");
        e2.calculateFinalPrice();
        e2.printData();
        e2.printInfo();
        
        Clothing c1 = new Clothing();
        Clothing c2 = new Clothing();
        c1.showcase("Leather Jacket", 5000);
        c1.Season("Winter");
        c1.calculateFinalPrice();
        c1.printData();
        c1.opPrint();
        c2.showcase("T-Shirt", 2500);
        c2.Season("Summer");
        c2.calculateFinalPrice();
        c2.printData();
        c2.opPrint();
    }
}

class Shop 
{
    String productName;
    double price;
    
    void showcase(String pn, double p) 
    {
        productName = pn;
        price = p;
    }
    
    void printData() 
    {
        System.out.println("PRODUCT NAME: " + productName + '\n' + "PRICE: " + price);
    }
}

class Electronics extends Shop 
{
    String warrantyPeriod;
    
    void displayData(String w) 
    {
        warrantyPeriod = w;
    }
    
    void printInfo() 
    {
        System.out.println("WARRANTY PERIOD: " + warrantyPeriod);
    }
    
    public void calculateFinalPrice() 
    {
        double discount = 0.10;// 10/100
        double discountedPrice = price - (price * discount);
        this.price = discountedPrice;
    }
}

class Clothing extends Shop 
{
    String season;
    
    void Season(String s) 
    {
        season = s;
    }
    
    void opPrint() 
    {
        System.out.println("SEASON: " + season);
    }
    
    public void calculateFinalPrice() 
    {
        double discount = 0.15; // 15/100
        double discountedPrice = price - (price * discount);
        this.price = discountedPrice;
    }
}
