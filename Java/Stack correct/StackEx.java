import java.util.Scanner;
class StackEx {
    public static void main(String[] args) 
    {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the number of elements to push: ");
        int n = input.nextInt();
        
        Stack s = new Stack();
        System.out.println("Enter " + n + " elements to push into the stack:");
        for (int i = 0; i < n; i++) 
        {
            System.out.print("Enter "+(i+1)+" element: ");
            int element = input.nextInt();
            s.push(element);
        }
        System.out.println("Push: ");
        s.print();
        System.out.println("Peek: "+s.peek());
        s.peek();
        System.out.println("Pop: ");
        s.pop();
        s.print();
    }
}

class Stack 
{
    int capacity = 1000;
    int top = -1;
    int a[] = new int[capacity];
    
    void push(int x) 
    {
        top++;
        if (top >= capacity) 
        {
            System.out.println("Stack overflow");
            top--;
            return;
        }
        a[top] = x;
        
    }
    int pop() 
    {
        if (top < 0) 
        {
            System.out.println("Stack underflow");
            return 0;
        } 
        else 
        {
            int x = a[top];
            top--;
            return x;
        }
    }
    int peek() 
    {
        if (top < 0) 
        {
            System.out.println("Stack underflow");
            return 0;
        } 
        else 
        {
           
            return a[top];
        }
    }
    void print()
    {
        for(int i=top;i>-1;i--)
        {
            System.out.println(a[i]);
            
        }
    }
}
