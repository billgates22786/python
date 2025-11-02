import java.util.Scanner;
class LinkedList3
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
            List.insert(input.nextInt());
        }
        List.printlist();
        System.out.print('\n'+"Enter the new element in front: ");
        List.insert(input.nextInt());
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
           newNode.next = head;
           head = newNode;
        }
    }

    void printlist()
    {
        Node CurrentNode = head;
        System.out.println("LINKEDLIST: ");
        while (CurrentNode != null) 
        {
            System.out.print(CurrentNode.data + " ");
            CurrentNode = CurrentNode.next;
        }
    }
}