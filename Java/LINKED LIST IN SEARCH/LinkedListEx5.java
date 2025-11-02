import java.util.Scanner;
class LinkedListEx5 
{
    public static void main(String[] a) 
    {
        int n;
        LinkedList list = new LinkedList();
        Scanner input = new Scanner(System.in);
        System.out.print("Enter no.of elements : ");
        n = input.nextInt();
        System.out.println("Enter "+n+" elements: ");
        for (int i = 0; i < n; i++) 
        {
            System.out.print("Enter "+(i+1)+" element: ");
            list.insert(input.nextInt());
        }
        list.printList();
        System.out.print("\nEnter element to search: ");
        int index = list.search(input.nextInt());
        if (index == -1) 
        {
            System.out.println("Element not found");
        } else 
        {
            System.out.println("Element found at index " + index);
        }
        list.printList();
    }
}

class Node 
{
    int data;
    Node next;
    Node(int d) 
    {
        data = d;
    }
}
class LinkedList 
{
    Node head;
    void insertStart(int data) {
        Node newNode = new Node(data);
        if (head == null) 
        {
            head = newNode;
        }
        else 
        {
            newNode.next = head;
            head = newNode;
        }
    }
    void insert(int data) {
        Node newNode = new Node(data);

        if (head == null) {
            head = newNode;
        }
        else 
        {
            Node last = head;
            while (last.next != null) 
            {
                last = last.next;
            }
            last.next = newNode;
        }

    }

    int search(int data) 
    {
        int pos = -1;
        int counter = 0;

        Node currNode = head;
        while (currNode.next != null) 
        {
            if (currNode.data == data) 
            {
                pos = counter;
                break;
            } else 
            {
                currNode = currNode.next;
                counter++;
            }
        }
        return pos;
    }

    void printList() 
    {
        Node currNode = head;
        System.out.print("LinkedList: ");
        while (currNode != null) 
        {
            System.out.print(currNode.data + " ");
            currNode = currNode.next;
        }
    }
}