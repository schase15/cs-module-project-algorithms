'''
Understand:
    Input: a List of integers
    Returns: a List of integers, with all of the zeros on the far right and the other integers on the left
            Order of non-zero integers doesn't matter
'''

'''
Plan:
    Iterate through the array, if the value is non-zero, remove it and add it to the front
    Return the array with all of the non-zeros at the front
'''

# Space complexity is O(1), only uses the input array
# Runtime complexity is O(n)

def moving_zeroes(arr):
    # Iterate through the array
    for value in arr:   # O(n)
        # If the value is not equal to 0, remove and add it to the front
        if value != 0:  # O(1)
            arr.remove(value)   # O(1)
            arr.insert(0, value)    # O(1)
        # Otherwise, do nothing

    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
