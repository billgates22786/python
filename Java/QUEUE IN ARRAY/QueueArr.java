import java.util.Scanner;
class QueueArr 
{
    public static void main(String[] args) 
    {
        Scanner input = new Scanner(System.in);
        Queue queue = new Queue();
        int i;
        System.out.print("Enter number of elements in array: ");
        int n = input.nextInt();
        for (i = 0; i < n; i++) 
        {
            System.out.print("Enter "+(i+1)+" element: ");
            int element = input.nextInt();
            queue.enqueue(element);
        }
        System.out.println("Front element is: " + queue.peek());
        System.out.println("Front element is: " + queue.peek());
        System.out.println("Enter number of elements after deletion: ");
        int k = input.nextInt();
        for (i = 0; i < k; i++) 
        {
            queue.dequeue();
        }
        queue.print();
        System.out.println("\nQueue size is " + queue.size());
        if (queue.isEmpty()) 
        {
            System.out.println("Queue is empty.");
        } 
        else 
        {
            System.out.println("Queue is not empty.");
        }
    }
}
class Queue 
{
    private int[] a;
    private int front;
    private int rear;
    private int capacity = 5;

    Queue() 
    {
        a = new int[capacity];
        front = 0;
        rear = -1;
    }

    void enqueue(int item) 
    {
        if (isFull()) 
        {
            System.out.println("Queue is full. Cannot enqueue element.");
            return;
        }
        rear++;
        a[rear] = item;
        System.out.println("Inserted " + item);
    }

    void dequeue() 
    {
        if (isEmpty()) 
        {
            System.out.println("Queue is empty. No element to dequeue.");
            return;
        }
        System.out.println("Removed " + a[front]);
        for (int i = 0; i < rear; i++) 
        {
            a[i] = a[i + 1];
        }
        rear--;
    }
    int peek() 
    {
        if (isEmpty()) 
        {
            System.out.println("Queue is empty.");
            return -1;
        }
        return a[front];
    }

    int size() 
    {
        return rear - front + 1;
    }
    boolean isEmpty() 
    {
        return rear < front;
    }
    boolean isFull() 
    {
        return rear == capacity - 1;
    }
    void print() 
    {
        System.out.print("Queue = ");
        for (int i = front; i <= rear; i++) 
        {
            System.out.print(a[i] + " ");
        }
    }
}
