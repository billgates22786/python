import java.util.Scanner;
class Vehicle_Rental_System 
{
    public static void main(String[] args) 
    {
        Scanner input = new Scanner(System.in);
        System.out.print("ENTER NUMBER OF DAYS: ");
        int rentalDays = input.nextInt();
       
        Car c = new Car("PB 33 EE 3333", 4000);
        double carCharge = c.rentalCharge(rentalDays);
        c.display();
        System.out.println("Car Rental charge for " + rentalDays + " days: " + carCharge);
    
        Bike b = new Bike("PB 33 KJ 2005", 2580);
        double bikeCharge = b.rentalCharge(rentalDays);
        b.display();
        System.out.println("Bike Rental charge for " + rentalDays + " days: " + bikeCharge);

        Truck t = new Truck("PB 33 SH 1877", 6000);
        double truckCharge = t.rentalCharge(rentalDays);
        t.display();
        System.out.println("Truck Rental charge for " + rentalDays + " days: " + truckCharge);
    }
}

class Vehicle 
{
    String registrationNumber; 
    double rentalRate;

    Vehicle(String r, double re) 
    {
        registrationNumber = r; 
        rentalRate = re; 
    }
      void display()
    {
        System.out.println("Vehicle Number: "+registrationNumber);
    }
    double rentalCharge(int days) 
    {
        return days * rentalRate;
    }
}

class Car extends Vehicle 
{
    double extraCharge = 1000.00;
    
    Car(String r, double re) 
    {
        super(r, re);
    }
    double rentalCharge(int days) 
    {
        return super.rentalCharge(days) + extraCharge;
    }
}

class Bike extends Vehicle 
{
    Bike(String r, double re) 
    {
        super(r, re);
    }
    double rentalCharge(int days) 
    {
        return super.rentalCharge(days);
    }
}

class Truck extends Vehicle 
{
    double extraCharge = 500.00;
    
    Truck(String r, double re) 
    {
        super(r, re);
    }
    double rentalCharge(int days) 
    {
        return super.rentalCharge(days) + extraCharge;
    }
}
