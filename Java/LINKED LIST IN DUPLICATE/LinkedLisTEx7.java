import java.util.Scanner;
class LinkedLisTEx7
{
    public static void main(String[] args)
    {
     Scanner sc=new Scanner(System.in);
     LinkedList list=new LinkedList();
     int n;
     System.out.print("Enter the number of elements:");
     n=sc.nextInt();
     System.out.printf("Enter %d elements:",n);
     for(int i=0;i<n;i++){
        int data=sc.nextInt();
        list.insert(data);
        }

        list.print();
    System.out.println("\nEnter an element you want to delete:");
    list.duplicate();
    list.print();
    }
}
class Node
{
    int data;
    Node next;
    Node(int d)
    {
     data=d;
    }
}
class LinkedList
{
    Node head;

     void duplicate()
    {
        Node currNode=head;
    
        while(currNode!=null && currNode.next!=null)
        {
            Node newNode=currNode.next;
            if(currNode.data==newNode.data)
            {
                currNode.next=newNode.next;
                
            }
            else
            {
            currNode=newNode;
            }
            
        }
    }


    void insert(int data)
    {
        Node newNode=new Node(data);

        if(head==null)
        {
            head=newNode;
        }
        else
        {
            Node last=head;
            while(last.next!=null)
            {
                last=last.next;
            }
            last.next=newNode;
        }
    }
   

    void print()
    {
        Node currNode=head;
        System.out.print("Linked List:");
        while(currNode!=null)
        {
            System.out.print(currNode.data+" ");
            currNode=currNode.next;

        }

    }

}