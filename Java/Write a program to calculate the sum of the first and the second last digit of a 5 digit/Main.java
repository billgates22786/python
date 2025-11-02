class Main {
    public static void main(String[] args) 
    {
        int a = 25896;
        int First_Digit =  a/ 10000;
        int Second_Last_Digit = (a/ 10) % 10;
        int sum = First_Digit + Second_Last_Digit;
        System.out.println("\u0007");
        System.out.println("Sum of the first and second last digit:- " + sum);
         System.out.println("\u0007");
    }
}
