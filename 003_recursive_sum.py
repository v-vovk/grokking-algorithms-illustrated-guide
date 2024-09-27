def sum(arr):
    # Recursive sum algorithm:
    # 1. If the array is empty, return 0.
    # 2. Otherwise, return the first element plus the sum of the rest of the array.
    # Time complexity: O(n)
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + sum(arr[1:])

print(sum([1, 2, 3, 4, 5]))  # 15