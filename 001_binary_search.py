def binary_search(list, item):
    # Binary search algorithm:
    # 1. Set the initial low and high pointers to the start and end of the list.
    # 2. While the low pointer is less than or equal to the high pointer:
    #    a. Calculate the mid-point.
    #    b. If the mid-point value is equal to the item, return the mid-point index.
    #    c. If the mid-point value is greater than the item, move the high pointer to mid-point - 1.
    #    d. If the mid-point value is less than the item, move the low pointer to mid-point + 1.
    # 3. If the item is not found, return None.
    # Time complexity: O(log n)
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]

        if guess == item:
            return mid

        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None


my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))  # => 1
print(binary_search(my_list, -1))  # => None