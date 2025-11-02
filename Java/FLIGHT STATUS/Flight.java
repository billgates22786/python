class Airplane{
    private String flightNumber;
    private String destination;
    private String scheduledDeparture;  
    private int delayTime;
    
    public Airplane(String fn, String d, String sd){
        flightNumber = fn;
        destination = d;
        scheduledDeparture = sd;
        delayTime = 0;
    };
    
    public void setDelayTime(int delay){
        delayTime = delay;
    };
    public void Status(){
        System.out.println("Flight "+flightNumber+ "is on time");
    };
    
    public String getFlightStatus(){
        if (delayTime > 0){
            return "delayed by " + delayTime + " minutes";
        } else {
            return "on time";
        }
    };
    public void flightStatus(){
        System.out.println("Flight " + flightNumber + " is " + getFlightStatus() + ".");
    };
}

class Flight{
    public static void main(String [] args){
        Airplane flight1 = new Airplane("CDE345", "New York", "14:00");
        Airplane flight2 = new Airplane("KUI765", "London", "15:30");
        Airplane flight3 = new Airplane("JUY456", "USA", "16:45");
        
        flight1.setDelayTime(40);
        flight2.setDelayTime(110);
        
        System.out.println("Flight status:");
        flight1.Status();
        flight2.Status();
        flight3.Status();
        
        System.out.println("Current Flight status:");
        flight1.flightStatus();
        flight2.flightStatus();
        flight3.flightStatus();
    }
}
