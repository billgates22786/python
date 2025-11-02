import java.util.Scanner;
class LinkedList1
{
    public static void main(String[] args)
    {
        int n;
        LinkedList List = new LinkedList();
        Scanner input = new Scanner(System.in);
        System.out.print("Enter no. of elements: ");
        n = input.nextInt();
        System.out.println("Enter "+n+" elements: ");
        for(int i =0;i<n;i++)
        {
            System.out.print("Enter "+(i+1)+" element: ");
            int data = input.nextInt();
            List.insert(data);
        }
        List.printlist();
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
    void insert(int data)
    {
        Node newNode = new Node(data);
        
        if(head == null)
        {
            head = newNode;
        }
        else 
        {
            Node last = head;
            while(last.next != null)
            {
                last = last.next;
            }
            last.next = newNode;
        }
    }

    void printlist()
    {
        Node CurrentNode = head;
        System.err.print("LINKEDLIST: ");
        while (CurrentNode != null) 
        {
            System.out.print(CurrentNode.data + " ");
            CurrentNode = CurrentNode.next;
        }
    }
}