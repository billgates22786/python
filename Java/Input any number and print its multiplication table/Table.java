import java.util.Scanner;
class Table {
    public static void main(String[] args) {
        int a;
        Scanner input = new Scanner(System.in);
        System.out.print("ENTER THE NUMBER FOR MULTIPLICATION TABLE: ");
        a = input.nextInt();
        for(int i = 1; i <= 10; i++) {
            System.out.println(a + " * " + i + " = " + (a * i));
        }
    }
}
