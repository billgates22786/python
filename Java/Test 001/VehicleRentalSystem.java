public class VehicleRentalSystem 
{
    public static void main(String[] args) 
    {
        Car car = new Car("CAR001", 400.0);
        Bike bike = new Bike("BIKE001", 1000.0);
        Truck truck = new Truck("TRUCK001", 500.0);

   int rentalDays = 5;
        double carCharge = car.calculateRentalCharge(rentalDays);
        double bikeCharge = bike.calculateRentalCharge(rentalDays);
        double truckCharge = truck.calculateRentalCharge(rentalDays);

        // Displaying results
        System.out.println("Car rental for " + rentalDays + " days: Rs." + carCharge);
        System.out.println("Bike rental for " + rentalDays + " days: Rs." + bikeCharge);
        System.out.println("Truck rental for " + rentalDays + " days: Rs." + truckCharge);
    }
}
// Vehicle class - Base class
class Vehicle 
{
    private String registrationNumber;
    protected double rentalRate; // using protected to allow access in subclasses

    public Vehicle(String registrationNumber, double rentalRate) 
    {
        this.registrationNumber = registrationNumber;
        this.rentalRate = rentalRate;
    }

    public double calculateRentalCharge(int days) 
    {
        return rentalRate * days;
    }
}

// Car class - Subclass of Vehicle
class Car extends Vehicle 
{
    private static final double EXTRA_CHARGE = 500.0;

    public Car(String registrationNumber, double rentalRate) 
    {
        super(registrationNumber, rentalRate);
    }

    @Override
    public double calculateRentalCharge(int days) 
    {
        return super.calculateRentalCharge(days) + EXTRA_CHARGE;
    }
}

class Bike extends Vehicle 
{
    public Bike(String registrationNumber, double rentalRate) 
    {
        super(registrationNumber, rentalRate);
    }
   
}

class Truck extends Vehicle {
    private static final double EXTRA_CHARGE = 1000.0;

    public Truck(String registrationNumber, double rentalRate) 
    {
        super(registrationNumber, rentalRate);
    }

    @Override
    public double calculateRentalCharge(int days) 
    {
        return super.calculateRentalCharge(days) + EXTRA_CHARGE;
    }
}



