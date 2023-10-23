# A bubble sort can be modified to "bubble" in both directions. 
# The first pass moves "up" the list and the second pass moves "down." 
# This alternating pattern continues until no more passes are necessary. 
# Implement this variation and describe under what circumstances it might be appropriate.


def bidirectional_bubble_sort(arr):
    n = len(arr)
    swapped = True
    
    while swapped:
        swapped = False
        
        for i in range(0, n-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
        
        if not swapped:
            break
        
        swapped = False
        
        for i in range(n-2, -1, -1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True


if __name__ == "__main__":
    my_list = [64, 34, 25, 12, 22, 11, 90]
    bidirectional_bubble_sort(my_list)
    print("Sorted array is:", my_list)
