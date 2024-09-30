def quicksort(array):
    # Quicksort algorithm:
    # 1. Choose a pivot element from the array.
    # 2. Partition the array so that all elements less than the pivot come before it, and all elements greater come after it.
    # 3. Recursively apply the algorithm to the sub-arrays.
    # Time complexity: O(n log n)

    if len(array) < 2:
        return array # Base case: arrays with 0 or 1 element are already "sorted".
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot] # Sub-array of all the elements less than the pivot
        greater = [i for i in array[1:] if i > pivot] # Sub-array of all the elements greater than the pivot

        return quicksort(less) + [pivot] + quicksort(greater) # Recursion: return the sorted array

print(quicksort([10, 5, 2, 3])) # [2, 3, 5, 10]
