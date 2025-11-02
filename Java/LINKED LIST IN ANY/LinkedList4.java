import java.util.Scanner;
class LinkedList4
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
        System.out.print("\nEnter element you want to insert after: ");
        int elem = input.nextInt();
        System.out.print("Enter new element to insert: ");
        int newData = input.nextInt();
        List.insertAfter(elem, newData);
        System.out.println("\nLinked List after insertion:");
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
     void insertAfter( int elem, int data)
    {
        Node currNode = head;
        Node newNode = new Node(data);

        while(currNode!= null && currNode.data != elem)
        {
           currNode= currNode.next;
        } 
        if(currNode!=null)
        {
            newNode.next= currNode.next;
            currNode.next= newNode;
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