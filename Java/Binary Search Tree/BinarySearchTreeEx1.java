import java.util.Scanner;
class BinarySearchTreeEx1 
{
    public static void main(String[] args) 
    {
        Scanner input = new Scanner(System.in);
        BinarySearchTree tree = new BinarySearchTree();
        System.out.print("Enter number of elements in array: ");
        int n = input.nextInt();
        for(int i=0;i<n;i++)
        {
            System.out.print("Enter "+(i+1)+" element: ");
            int k = input.nextInt();
            tree.insert(k);
        }
        System.out.println("Press 1 to intialize (InOrder)");
        System.out.println("Press 2 to intialize (PreOrder)");
        System.out.println("Press 3 to intialize (PostOrder)");
        System.out.print("Enter your choice: ");
        int c = input.nextInt();
        if(c==1)
        {
            System.out.println("In order: ");
            tree.inorder();
        }
        if(c==2)
        {
            System.out.println("In preorder: ");
            tree.preorder();
        }
        if(c==3)
        {
            System.out.println("In postorder: ");
            tree.postorder();
        }
    }
}
class Node 
{
    int data;
    Node left;
    Node right;
    Node(int d) 
    {
        data = d;
    }
}

class BinarySearchTree 
{
    Node root;
    void insert(int data) 
    {
        root = insertRec(root, data);
    }
    Node insertRec(Node root, int data) 
    {
        Node newNode = new Node(data);
        if (root == null) 
        {
            root = newNode;
        } else if (data < root.data) {
            root.left = insertRec(root.left, data);
        } else if (data > root.data) {
            root.right = insertRec(root.right, data);
        }
        return root;
    }
    void inorder()
    {
        inorderRec(root);
    }
    void inorderRec(Node root)
    {
        if(root!=null)
        {
            inorderRec(root.left);
            System.out.println(root.data+" ");
            inorderRec(root.right);
        }
    }
    void preorder()
    {
        preorderRec(root);
    }
    void preorderRec(Node root)
    {
        if(root!=null)
        {
            System.out.println(root.data+" ");
            inorderRec(root.left);
            inorderRec(root.right);
        }
    }
    void postorder()
    {
        postorderRec(root);
    }
    void postorderRec(Node root)
    {
      if(root!=null)
        {
            inorderRec(root.left);
            inorderRec(root.right);
            System.out.println(root.data+" ");
        }  
    }
}