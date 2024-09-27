def find_smallest(arr):
    # This function finds the smallest element in the array and returns its index.
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index

# Selection sort algorithm:
# 1. Find the smallest element in the array.
# 2. Remove the smallest element from the original array and add it to a new array.
# 3. Repeat the process until all elements are sorted.
# Time complexity: O(n^2)
def selection_sort(arr):
    new_arr = []

    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))

    return new_arr

print(selection_sort([5, 3, 6, 2, 10]))  # [2, 3, 5, 6, 10]