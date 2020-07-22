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




def single_number(arr):
    # Define empty array
    single = []
    # iterate through the array
    for item in arr:

        # if item is already in the single array, remove it from the array
        if item in single:
            single.remove(item)
        # If it is not in the array yet, add it
        else:
            single.append(item)
    
    # Return the one value in the single list
    return single[0]
    


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
    