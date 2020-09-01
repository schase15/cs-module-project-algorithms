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
    for i in range((len(nums)-k) +1):   #O (n)
        # Create sliding window array
        window = nums[i: i + k]     # O(1)
        # Find the max value in the window and add it to the solution array
        solution.append(max(window))    #O(1) - append, O(n) - max()
    
    # return the solutions array
    return solution


'''
Second Pass Plan:
    Run time of first pass solution is O(n^2), because max() method is O(n) and is inside the for loop which is O(n)
    Find a more efficient method to find the max
        Sort the list and return the last one, same runtime
    

'''
##### This doesn't work because I forgot that the window isn't set at 3, it is variable length k so would require another for loop which makes it O(n)
# Runtime is O(n)
# Space complexity is O(n)

# def sliding_window_max(nums, k):

#     # Create an empty solutions array
#     solution = []

#     # Move the sliding window from the front of the nums array until it hits the back
#     for i in range((len(nums)-k) +1):   #O (n)
#         # Create sliding window array
#         window = nums[i: i + k]     # O(1)

#         # Each window array only has k items
#         # create if statements, create temp max variable = window[1]
#         # if item 2 is greater than max_value, replace max_value
#         # If item 3 is greater than max_value, replace max_value
#         # Append max value to solutions array

#         max_value = window[0]

#         if window[1] > max_value:   # O(1)
#             max_value = window[1]

#         if window[2] > max_value:   # O(1)
#             max_value = window[2]

#         solution.append(max_value)  # O(1)


#     # return the solutions array
#     return solution


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
