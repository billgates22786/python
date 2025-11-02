import java.util.Scanner;
class LinkedListEx6
{
    public static void main(String [] a)
    {
     int n;
     LinkedList list = new LinkedList();
     Scanner sc= new Scanner(System.in);
     System.out.print("Enter no.of elements : ");
     n= sc.nextInt();
     System.out.println("Enter "+n+" elements: ");
     for(int i=0;i<n;i++)
        {
            System.out.print("Enter "+(i+1)+" element: ");
            list.insert(sc.nextInt());
        }
    list.printList();
    System.out.println("\nEnter element you want to delete ");
    list.delete(sc.nextInt());
    System.out.println("\nLinked List after deletion is :");
    list.printList(); 
    } 
}

class Node
{
    int data;
    Node next;
    Node(int d)
    {
        data= d;
    }
}

class LinkedList
{
    Node head;
    void insertStart( int data)
    {
        Node newNode = new Node(data);
        
        if(head==null)
        {
        head= newNode;
        }
        else
        {
           
            newNode.next = head;
            head= newNode;
        }
    }
    void insert( int data)
    {
        Node newNode = new Node(data);
        if(head==null)
        {
        head= newNode;
        }
        else
        {
            Node last = head;
            while(last.next!=null)
            {
                last = last.next;
            }
            last.next= newNode;
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
     void delete( int data)
    {
        Node currNode = head;
        Node prevNode = null;

        while(currNode!= null && currNode.data != data)
        {
           prevNode= currNode;
           currNode= currNode.next;
        } 
        if(currNode!=null)
        {
            if(currNode.next==null)
            {
                head= null; 
            }
            else if(prevNode==null)
            {
                head = currNode.next; 
            }
            else
            {
                prevNode.next = currNode.next;
            }
        }   
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