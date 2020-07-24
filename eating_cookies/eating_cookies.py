'''
Understand:
    Input: an integer, the amount of cookie in the jar
    Returns: an integer, the total number of different ways he can eat all the cookies in the jar
'''

'''
Rules:
He can eat up to 3 cookies at once
He can eat in any combination of 1, 2 or 3 cookies at a time to finish the jar with n cookies
'''

'''
Plan:
    Start with him eating all the cookies in the jar in the smallest amount, mostly 3 at a time
    recursively call the method that subtracts 1 from the 3
    Keep going until he is eating the cookies all 1 at a time

Use recursion:
Base cases:
    He is eating all single cookies
    He is eating 0 cookies
    He is eating negative cookies

Move towards the base case by subtracting 1, 2 or 3 from the cookie jar. He can up to 3 cookies at a time.
'''


# def eating_cookies(n):
#     # Base cases:
    
#     # If n is negative, return 0
#     if n < 0:
#         return 0

#     # If n is 1 or zero return 1, there is one way to eat cookies of that amount
#     if n <= 1 :
#         return 1

#     # Recursive case: if it is more than 1, move it closer to the base case
#     # Use recursive calls to break down eating in batches of 1, 2 and 3
#     return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)


'''
More efficient method
'''

'''
How do we reduce the amount of redundant work?
Use a data structure to 'cache' (or 'save') answers that some other branch has already done
Someone still has to figure out the answer in the first place but once that answer is computed, 
we'll share that answer with any other branch that needs to calculate the same thing
branches that need an answer that's already been computed can check the cache to see if the answer 
is already in there and just pull it out

What data structure should we use for the cache?
Save the n value for the branch along with its associated answer
Save the n value as a key and the associated answer as its value in a dictionary
we'll need to pass the dict to each recursive call
'''

# This cuts out all of the redundant work, every n value is now only computed once
# The cache reduced the runtime from O(3^n) down to O(n)
# We did increase space complexity 


def eating_cookies(n, cache= None):
    # Base cases:
    
    # If n is negative, return 0
    if n < 0:
        return 0

    # If n is 1 or zero return 1, there is one way to eat cookies of that amount
    if n == 0 :
        return 1

    # Create cache to store perviously solved answers
    if cache is None:
        cache = {}

    # Check the cache to see if it already holds the answer this branch is looking for
    if n in cache:
        # If n is in cache, return its associated answer
        return cache[n]

        # Otherwise, n is not in the cache, so we need to compute the answer and save it to the cache
    else:
        cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)

    return cache[n]



if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
