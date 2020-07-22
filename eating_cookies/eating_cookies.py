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

Move towards the base case by subtracting 1 from the cookie jar
'''


def eating_cookies(n):
    # Your code here

    pass

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
