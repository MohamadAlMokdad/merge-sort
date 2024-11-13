def merge_sort(arr):
    # Base case: if array is of length 1 or 0, it's already sorted
    if len(arr) > 1:
        # Find the middle point to divide the array into two halves
        mid = len(arr) // 2
        left_half = arr[:mid]   # Left half of the array
        right_half = arr[mid:]  # Right half of the array

        # Recursively sort both halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Initialize pointers for left_half, right_half, and merged array
        i = j = k = 0

        # Merge the sorted halves back into the main array
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Copy remaining elements of left_half, if any
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Copy remaining elements of right_half, if any
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print("Merge Sorted array:", sorted_arr)
