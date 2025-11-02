import java.util.Arrays;
import java.util.Scanner;
class BinarySearchTreeEx 
{

    public static void main(String[] args) 
    {
        Scanner input = new Scanner(System.in);
        BinarySearchTree bst = new BinarySearchTree(10);
        System.out.print("Enter number of elements in an array: ");
        int n = input.nextInt();
        if(n<=100)
        {
            for(int i=0;i<n;i++)
            {
                int k = input.nextInt();
                bst.insert(k);
            }
        System.out.println("Inorder traversal of the BST: ");
        bst.inorderTr aversal();
        }
        else
        {
            System.out.println("Wrong attempt");
        }
       
    }
}

class BinarySearchTree 
{

    private int[] tree;
    private int size;

    public BinarySearchTree(int n) 
    {
        tree = new int[100];
        Arrays.fill(tree, -1);
        size = 0;
    }

    public void insert(int data) 
    {
        if (size == 0) 
        {
            tree[0] = data;
            size++;
        } 
        else 
        {
            insertRec(0, data);
        }
    }

    private void insertRec(int index, int data) {

        if (tree[index] == -1) 
        {
            tree[index] = data;
            size++;
        } 
        else if (data < tree[index]) 
        {
            insertRec(2 * index + 1, data);
        } 
        else if (data > tree[index]) 
        {
            insertRec(2 * index + 2, data);
        }
    }

    public void inorderTraversal() 
    {
        inorderRec(0);
    }

    private void inorderRec(int index) 
    {
        if (index < tree.length && tree[index] != -1) 
        {
            inorderRec(2 * index + 1);
            System.out.print(tree[index] + " ");
            inorderRec(2 * index + 2);
        }
    }

}