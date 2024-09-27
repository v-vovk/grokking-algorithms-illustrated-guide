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

def count_items(arr):
    # Recursive count algorithm:
    # 1. If the array is empty, return 0.
    # 2. Otherwise, return 1 plus the count of the rest of the array.
    # Time complexity: O(n)
    if len(arr) == 0:
        return 0
    else:
        return 1 + count_items(arr[1:])

print(count_items([1, 2, 3, 4, 5]))  # 5

def max_value(arr):
    # Recursive max algorithm:
    # 1. If the array has only one element, return that element.
    # 2. Otherwise, return the maximum of the first element and the maximum of the rest of the array.
    # Time complexity: O(n)
    if len(arr) == 1:
        return arr[0]
    else:
        return max(arr[0], max_value(arr[1:]))

print(max_value([1, 2, 3, 4, 5]))  # 5