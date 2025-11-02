import java.util.Scanner;
class Temperature 
{
    public static void main(String[] args) 
    {
        float celsius, fahrenheit;
        Scanner input = new Scanner(System.in);
        System.out.print("ENTER THE TEMPERATURE IN FAHRENHEIT:- ");
        fahrenheit = input.nextInt();
        celsius = (float)((fahrenheit - 32) *0.55);
        System.out.println("CELSIUS TEMPERATURE:-" + celsius);
    }
}
