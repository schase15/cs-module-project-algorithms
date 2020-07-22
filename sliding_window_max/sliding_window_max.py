'''
Understand:
    Input: a List of integers as well as an integer `k` representing the size of the sliding window
    Returns: a List of integers, the max of the window when the first element of the window is at that index position
'''

'''
Plan:
    Iterate through i for range(len(nums))
        Only move the window until the last element is at the end of the list
            range((len(nums)-k) +1)
    The begining of the window is at index i
        The window includes nums[i: i + k]
    Use this to create a new sliding window each time
        Find the max of the current sliding window and add it to a solution array
'''



def sliding_window_max(nums, k):
    # Create an empty solutions array
    solution = []

    # Move the sliding window from the front of the nums array until it hits the back
    for i in range((len(nums)-k) +1):
        # Create sliding window array
        window = nums[i: i + k]
        # Find the max value in the window and add it to the solution array
        solution.append(max(window))
    
    # return the solutions array
    return solution


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
