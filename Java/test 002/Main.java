// Vehicle.java (Base Class)
class Vehicle {
    String registrationNumber;
    double rentalRate;

    Vehicle(String registrationNumber, double rentalRate) {
        this.registrationNumber = registrationNumber;
        this.rentalRate = rentalRate;
    }

    double calculateRentalCharge(int days) {
        return days * rentalRate;
    }
}

// Car.java (Subclass of Vehicle)
class Car extends Vehicle {
    static final double EXTRA_CHARGE = 1000.0; // Fixed extra charge for cars

    Car(String registrationNumber, double rentalRate) {
        super(registrationNumber, rentalRate);
    }

    @Override
    double calculateRentalCharge(int days) {
        return super.calculateRentalCharge(days) + EXTRA_CHARGE;
    }
}

// Bike.java (Subclass of Vehicle)
class Bike extends Vehicle {
    Bike(String registrationNumber, double rentalRate) {
        super(registrationNumber, rentalRate);
    }
}

// Truck.java (Subclass of Vehicle)
class Truck extends Vehicle {
    static final double EXTRA_CHARGE = 500.0; // Fixed extra charge for trucks

    Truck(String registrationNumber, double rentalRate) {
        super(registrationNumber, rentalRate);
    }

    @Override
    double calculateRentalCharge(int days) {
        return super.calculateRentalCharge(days) + EXTRA_CHARGE;
    }
}

// Main.java (Program Entry Point)
public class Main {
    public static void main(String[] args) {
        int rentalDays = 5; // Example rental duration

        Car car = new Car("MH 01 AB 1234", 100.0);
        Bike bike = new Bike("MH 02 CD 5678", 1000.0);
        Truck truck = new Truck("MH 03 EF 9012", 200.0);

        System.out.println("Car rental for " + rentalDays + " days: Rs." + car.calculateRentalCharge(rentalDays));
        System.out.println("Bike rental for " + rentalDays + " days: Rs." + bike.calculateRentalCharge(rentalDays));
        System.out.println("Truck rental for " + rentalDays + " days: Rs." + truck.calculateRentalCharge(rentalDays));
    }
}
