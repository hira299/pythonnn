def linear_search(lst, element):
    """Perform a linear search on the list for the given element."""
    for x in range(len(lst)):
        if lst[x] == element:
            return x  # Return the position (index) of the element
    return 'not found'  # If the element is not in the list, return 'not found'

# Example usage
my_list = [4, 2, 7, 1, 3, 5]
element_to_find = 7

# Perform linear search
result = linear_search(my_list, element_to_find)

# Print the result
if result == 'not found':
    print(f"The element {element_to_find} was not found in the list.")
else:
    print(f"The element {element_to_find} is at position {result} in the list.")
