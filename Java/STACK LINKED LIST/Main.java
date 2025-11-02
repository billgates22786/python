class StackLinkedList {
    public static void main(String[] args) {

        Stack s = new Stack();
        s.push(10);
        s.push(20);
        s.push(30);
        s.print();
        System.out.println("After pop --- " + s.pop());
        s.print();
        System.out.println("Top element is " + s.peek());
        s.print();
    }
}

class Node {

    int data;
    Node next;

    Node(int d) {
        data = d;
    }
}

class Stack {

    Node top;

    void push(int data) {
        Node newNode = new Node(data);
        if (top == null) {
            top = newNode;
        } else {
            newNode.next = top;
            top = newNode;

        }
    }

    int pop() {
        if (top == null) {
            System.out.println("Stack is empty");
            return -1;
        } else {
            int data = top.data;
            top = top.next;
            return data;

        }
    }

    int peek() {
        if (top == null) {
            System.out.println("Stack is empty");
            return -1;
        } else {
            int data = top.data;
            return data;

        }
    }

    void print() {
        Node currNode = top;
        System.out.println("Stack = ");
        while (currNode != null) {
            System.out.println(currNode.data + " ");
            currNode = currNode.next;
        }
    }
}