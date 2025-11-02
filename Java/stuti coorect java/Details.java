class Vehicle 
{
    int registrationnumber;
    int rentrate;
    
    public void setData(int reg, int r) 
    {
        registrationnumber = reg;
        rentrate = r;
    }
    
    public void printData() 
    {
        System.out.println("Registration: " + registrationnumber + "\nRent rate: " + rentrate);
    }
    
    public int calculateRentalCharge(int days) 
    {
        if (days > 0) 
        {
            return days * rentrate;
        } else {
            return 0; 
        }
    }
}

class Car extends Vehicle 
{
    int extrachargeofcar;
    
    public void setData(int reg, int r, int e) 
    {
        super.setData(reg, r);
        extrachargeofcar = e;
    }
    
    public void printData() 
    {
        super.printData();
        System.out.println("Extra Charge For Cars: " + extrachargeofcar);
    }
    
    public int calculateRentalCharge(int days) 
    {
        return super.calculateRentalCharge(days) + extrachargeofcar;
    }
    
    public void displayFinalTotalChargeOfCar(int days) 
    {
        System.out.println("Car Rent for " + days + " days: Rs." + calculateRentalCharge(days));
    }
}

class Bike extends Vehicle 
{
    public void setData(int reg, int r) 
    {
        super.setData(reg, r);
    }
    
    public void printData() 
    {
        super.printData();
    }
    
    public void displayFinalTotalChargeOfBike(int days) 
    {
        System.out.println("Bike Rent for " + days + " days: Rs." + calculateRentalCharge(days));
    }
}

class Truck extends Vehicle 
{
    int extrachargeoftruck;
    
    public void setData(int reg, int r, int t) 
    {
        super.setData(reg, r);
        extrachargeoftruck = t;
    }
    
    public void printData() 
    {
        super.printData();
        System.out.println("Extra Charge For Trucks: " + extrachargeoftruck);
    }
    
    public int calculateRentalCharge(int days) 
    {
        return super.calculateRentalCharge(days) + extrachargeoftruck;
    }
    
    public void displayFinalTotalChargeOfTruck(int days) 
    {
        System.out.println("Truck Rent for " + days + " days: Rs. " + calculateRentalCharge(days));
    }
}

public class Details 
{
    public static void main(String[] args) 
    {
        Car c = new Car();
        c.setData(1234, 500, 300);
        c.printData();
        c.displayFinalTotalChargeOfCar(5);
        
        Bike b = new Bike();
        b.setData(1235, 400);
        b.printData();
        b.displayFinalTotalChargeOfBike(6);
        
        Truck t = new Truck();
        t.setData(1236, 600, 900);
        t.printData();
        t.displayFinalTotalChargeOfTruck(4);
    }
}
