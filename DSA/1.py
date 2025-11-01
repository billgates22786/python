arr = [10, 20, 30, 40, 50]
def traverse(arr):
    print("Array Elements:")
    for i in arr:
        print(i, end=" ")
    print("\n")
def insert(arr, element, position):
    arr.insert(position, element)
    print(f"After Insertion of {element} at position {position}: {arr}")
def delete(arr, position):
    removed = arr.pop(position)
    print(f"After Deletion of element {removed} from position {position}: {arr}")
print("Initial Array:", arr)
traverse(arr)
insert(arr, 25, 2)   
delete(arr, 3)       
print("\nFinal Array:")
traverse(arr)
