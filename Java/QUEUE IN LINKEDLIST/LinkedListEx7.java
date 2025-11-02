import java.util.Scanner;

class LinkedListEx7 
{
    public static void main(String[] args) 
    {
        Scanner input = new Scanner(System.in);
        Queue q = new Queue();
        System.out.print("Enter the number of elements to add: ");
        int n = input.nextInt();
        System.out.println("Enter the elements:");
        for (int i = 0; i < n; i++) 
        {
            int element = input.nextInt();
            q.enqueue(element);
        }
        System.out.println("Queue after enqueue:");
        q.print();
        System.out.println("Size of the queue after insertion: "+q.size());
        System.out.print("Enter the number of elements to delete: ");
        int k = input.nextInt();
        for (int i = 0; i < k; i++)
        {
            q.dequeue();
        }
        System.out.println("Queue after dequeue:");
        q.print();
        System.out.println("Size of the queue after deletion: "+q.size());
    }
}

class Node 
{
    int data;
    Node next;
    Node(int d) 
    {
        data = d;
        next = null;
    }
}

class Queue 
{
    Node front = null;
    Node rear = null;
    int size = 0;
    void dequeue() 
    {
        if (front == null) 
        {
            System.out.println("Queue is empty");
            return;
        } else 
        {
            front = front.next;
            size--;
            if (front == null) 
            {
                rear = null; 
            }
        }
    }
    
    void enqueue(int data) 
    {
        Node newNode = new Node(data);
        if (front == null) 
        {
            front = newNode;
            rear = newNode;
        } 
        else 
        {
            rear.next = newNode;
            rear = newNode;
        }
        size++;
    }
    void peek() 
    {
        if (front == null) 
        {
            System.out.println("Queue is empty");
        }
        else 
        {
            System.out.println(front.data);
        }
    }
    
    boolean isEmpty() 
    {
        return front == null;
    }
    
    int size() 
    {
        return size;
    }
    
    void print() 
    {
        if (front == null) 
        {
            System.out.println("Queue is empty");
            return;
        }
        Node currNode = front;
        while (currNode != null) 
        {
            System.out.print(currNode.data + " ");
            currNode = currNode.next;
        }
        System.out.println();
    }
}
