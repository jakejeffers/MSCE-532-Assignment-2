def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case: an array of 0 or 1 elements is already sorted
    
    pivot = arr[len(arr) // 2]  # Choose the pivot element
    left = [x for x in arr if x < pivot]  # Elements less than pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to pivot
    right = [x for x in arr if x > pivot]  # Elements greater than pivot
    
    return quick_sort(left) + middle + quick_sort(right)  # Recurse on left and right

arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)
