class Airplane 
{
    private String flightNumber;
    private String destination_location;
    private String scheduledDeparture;
    private int delayTime;
    public Airplane(String f, String d, String s) 
    {
        flightNumber = f;
        destination_location = d;
        scheduledDeparture = s;
        delayTime = 0;
    }

    public void setDelay(int delayTime) 
    {
        this.delayTime = delayTime;
    }

    public String FlightStatus() 
    {
        if (delayTime == 0) {
            return " FLIGHT TO "+ destination_location + " FLIGHT NUMBER " + flightNumber + " is on time.";
        } else {
            return " FLIGHT TO "+ destination_location + " FLIGHT NUMBER " + flightNumber + " is delayed by " + delayTime + " minutes.";
        }
    }

}
public class AirSchedule 
{
    public static void main(String[] args) 
    {
        Airplane a1 = new Airplane("CDE345", "New Delhi", "10:00 AM");
        Airplane a2 = new Airplane("KUI765", "Chennai", "12:00 PM");
        Airplane a3 = new Airplane("JUY456", "Chandigarh", "2:00 PM");
        System.out.println("Flight Status:");
        System.out.println(a1.FlightStatus());
        System.out.println(a2.FlightStatus());
        System.out.println(a3.FlightStatus());
        a1.setDelay(45);
        a2.setDelay(110);
        System.out.println("\nCurrent Flight Status:");
        System.out.println(a1.FlightStatus());
        System.out.println(a2.FlightStatus());
        System.out.println(a3.FlightStatus());
        System.out.println(" Mission accomplished! Time for cake. ");
    }
}