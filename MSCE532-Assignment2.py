def merge_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case: an array of 0 or 1 elements is already sorted
    
    # Find the middle of the array
    mid = len(arr) // 2
    left = arr[:mid]  # Left half
    right = arr[mid:]  # Right half

    # Recursively sort both halves
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    # Merge the two sorted halves
    return merge(left_sorted, right_sorted)

def merge(left, right):
    result = []
    i = j = 0

    # Merge while there are elements in both lists
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements from left or right
    result.extend(left[i:])
    result.extend(right[j:])
    return result
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Sorted array (can cause Quick Sort to degrade)
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)
