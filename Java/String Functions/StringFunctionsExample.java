public class StringFunctionsExample {
    public static void main(String[] args) 
    {
        String s = "Hello Surbhi Mam";
        System.out.println("String Length = " + s.length());
        System.out.println("First character = " + s.charAt(0));
        System.out.println("Substring from index 0 to 5 = " + s.substring(0, 5));
        System.out.println("Substring from index 12 to end = " + s.substring(12));
        System.out.println("Index of 'H' = " + s.indexOf('H'));
        System.out.println("Index of 'h' = " + s.indexOf('h'));
        System.out.println("String contains 'Mom'? = " + s.contains("Mom"));
    }
}
