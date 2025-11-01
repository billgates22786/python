def linear_search_1d(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  
    return -1  
my_list = [10, 23, 45, 70, 11, 15]
search_target = 70
result_1d = linear_search_1d(my_list, search_target)
if result_1d != -1:
    print(f"Element {search_target} found at index: {result_1d}")
else:
    print(f"Element {search_target} not found in the array.")
