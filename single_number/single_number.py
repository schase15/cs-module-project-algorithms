'''
Understand:
    Input: a List of integers where every int except one shows up twice
    Returns: the integer that only appears once in the list
'''

'''
Plan:
    Define an empty array
    Go through the input list, if the element doesn't already exist in the new array, add it
    If it does exist in the new array, remove it. 
    Add the end each element that is in the list twice will be added once, and the removed the second time it sees it
    The item that only appears once will be added but never removed
    Return that array which should only have 1 element by the end

'''

# Runtime O(n)
# Space complexity is O(n)

def single_number(arr):
    # Define empty array

    # As far as space complexity is concerned, worst case would be if we have half of the elements
    # in the array before we start removing them: O((1/2) * n) space complexity
    single = [] # O(1)
    # iterate through the array
    for item in arr:    # O(n)

        # if item is already in the single array, remove it from the array
        if item in single:  # O(1)
            single.remove(item) # O(1)
        # If it is not in the array yet, add it
        else:
            single.append(item)  # O(1)
    
    # Return the one value in the single list
    return single[0]    # O(1)


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
    