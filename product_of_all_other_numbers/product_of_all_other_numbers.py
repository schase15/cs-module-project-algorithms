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

def product_of_all_other_numbers(arr):

    # Create an array to store products
        # Create it the known length of the solution array, this saves space complexity
    solution = [0] * len(arr)

    # Iterate through each value in the array
    for i in range(len(arr)):
        # Split it into values before and after the index (not including the index)
        left = arr[:i]
        right = arr[i +1:]

        # Create a product variable that keeps track of the running product
        product = 1

        # Multiply the values on each side, updating the total product
        for value in left:
            product = product * value
        
        for value in right:
            product = product * value
        
        # Replace the placeholder value in the solution array at the proper index with the calculated product
        solution[i] = product
    
    # Return the solution array
    return solution


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
