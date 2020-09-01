'''
Understand:
    Input: a List of integers
    Returns: a List of products of the input array, not including the input value at its index spot
'''

'''
Plan:
    Iterate through each value in the array
    Calculate the product of all the other values other than its own
        Multiply all the values in the array to the left of the index
        Multiply all the values in the array to the right of the index
        Multipy those two together
        Return the final product
            Create a new array to store the solution in, changing in place will mess up future calculations         
'''

# def product_of_all_other_numbers(arr):

#     # Create an array to store products
#         # Create it the known length of the solution array, this saves space complexity
#     solution = [0] * len(arr)

#     # Iterate through each value in the array
#     for i in range(len(arr)):
#         # Split it into values before and after the index (not including the index)
#         left = arr[:i]
#         right = arr[i +1:]

#         # Create a product variable that keeps track of the running product
#         product = 1

#         # Multiply the values on each side, updating the total product
#         for value in left:
#             product = product * value
        
#         for value in right:
#             product = product * value
        
#         # Replace the placeholder value in the solution array at the proper index with the calculated product
#         solution[i] = product
    
#     # Return the solution array
#     return solution


'''
Optimize Plan:
    Get rid of the nested for loop by moving the the product loops outside the first loop
    Populate a solution array with 1 at every index
    Instead of appending each value into the solution list, multiply it into the existing product at that index location
        As we move through the index, the product has already been calculated for the values that come before it (except for the value immediately before it)

'''
# Runtime O(n)
# Space complexity is O(n)

def product_of_all_other_numbers(arr):

    # Create an array to store products
        # Create it the known length of the solution array, populate it with 1's so we can multiply values into it
    solution = [1] * len(arr)

    # Create an array to store the products of the left sides of each index location
    left_products = [1] * len(arr)

    # Do the same thing for the right side of the index
    right_products = [1] * len(arr)

    # Calculate the products of the left side of the arrays
    # The first value can be skipped because we are not including that in it's total product (same with the last for the right side)
    # Start at index 1, go through the end
    for i in range(1, len(arr)):
        # The left product at index i is the product of (the value before it * the product value we already calculated at that index spot)
        left_products[i] = arr[i-1] * left_products[i-1]

    # Do the same thing for the right side
    # Except you need to calculate from the back, buildiing off of the one which we know is the right product for the last index spot
    # Range(start, stop(does not include), step) 
    # - start at the second to last item, stop at 0 (so you have to use -1 because stop doesn't include), move backwards by taking -1 steps
    for i in range(len(arr)-2, -1, -1):
        # The right product at index i is the product of (the value after it and the product value we already calculated at that index spot)
        right_products[i] = arr[i+1] * right_products[i +1]

    # The product of the values to the left of the index are now stored in left_products
    # The product of the values to the right of the index are now stord in right_products
    # Create the solution array by multiplying them together at the index spot
    for i in range(len(arr)):
        solution[i] = left_products[i] * right_products[i]

    return solution 




if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
