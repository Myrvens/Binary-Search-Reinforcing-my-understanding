def binary_search(list, element):
    middle = 0
    start = 0
    end = len(list) - 1
    steps = 0

    while start <= end:
        steps += 1  # Increment steps at the start of the loop
        print("Step", steps, ":", str(list[start:end + 1]))
        
        middle = (start + end) // 2
        
        if element == list[middle]:  # Target found
            return middle
        if element < list[middle]:  # Narrow search to the left half
            end = middle - 1
        else:  # Narrow search to the right half
            start = middle + 1

    return -1  # Target not found

# Example usage
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 9
binary_search(my_list, target)