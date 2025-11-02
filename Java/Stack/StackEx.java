class StackEx {
    public static void main(String args[]) {
        Stack s = new Stack();
        s.push(10);
        s.push(20);
        s.push(30);

        System.out.print("Elements in stack: ");
        s.print();

        System.out.println("\n" + s.pop() + " Popped from stack");
        s.print();

        System.out.println("\nTop element is: " + s.peek());
    }
}

class Stack {
    static final int capacity = 10;
    int top = -1;
    int a[] = new int[capacity];

    void push(int x) {
        top++; // Increment top first
        if (top >= capacity) { // Check for overflow
            System.out.println("Stack overflow");
            top--; // Decrement top if overflow occurs
            return; // Exit the function
        }
        a[top] = x;
        System.out.println(x + " pushed into stack");
    }

    int pop() {
        if (top < 0) {
            System.out.println("Stack underflow");
            return 0;
        } else {
            int x = a[top];
            top--;
            return x;
        }
    }

    int peek() {
        if (top < 0) {
            System.out.println("Stack underflow");
            return 0;
        } else {
            return a[top];
        }
    }

    void print() {
        for (int i = top; i >= 0; i--) {
            System.out.print(a[i]); 
            // if (i != 0) {  // Add a space if it's not the last element
            //     System.out.print(" ");
            // }
        }
    }
}
