# Exercise 1
def sum_digits(num: int) -> int:
    """
    Separate each digit of the input and sum the digits together using recursion.

    Parameters:
    - num (int): The num to be recursively called

    Returns:
    int

    Examples:
    >>> sum_digits(1) 
    1
    >>> sum_digits(10) #returns 1 + 0
    1
    >>> sum_digits(111) #returns 1 + 1 + 1
    3
    >>> sum_digits(1234) #returns 1 + 2 + 3 + 4
    10
    >>> sum_digits(74219) #returns 7 + 4 + 2 + 1 + 9
    23
    """
    if num < 10:
        return num
    else:
        return num % 10 + (sum_digits(num // 10))

# Exercise 2
def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two positive integers using recursion.

    Parameters:
    - a (int): The first positive integer
    - b (int): The second positive integer

    Returns:
    int

    Examples:
    >>> gcd(48, 18) 
    6
    >>> gcd(54, 24) 
    6
    >>> gcd(101, 103) 
    1
    >>> gcd(56, 98) 
    14
    >>> gcd(100, 75) 
    25
    """
    if b == 0:
        return a
    else:
        return gcd(b, a%b)



# Exercise 3
def decimal_to_binary(n: int) -> str:
    """
    Convert a non-negative integer to its binary representation using recursion.

    Parameters:
    - n (int): The non-negative integer to be converted

    Returns:
    str

    Examples:
    >>> decimal_to_binary(10)
    '1010'
    >>> decimal_to_binary(7)
    '111'
    >>> decimal_to_binary(0)
    '0'
    >>> decimal_to_binary(1)
    '1'
    >>> decimal_to_binary(20)
    '10100'
    """
    if n == 0:
        return str(0)
    elif n == 1:
        return str(1)
    else:
        return str(decimal_to_binary(n // 2)) + str(decimal_to_binary(n % 2))
    


# Exercise 4
def max_depth(lst):
    """
    Find the maximum depth of nested lists using recursion and a helper function.

    Parameters:
    - lst (list): A list which may contain nested lists of integers

    Returns:
    int

    Examples:
    >>> max_depth([1, 2, 3])
    1
    >>> max_depth([1, [2, [3, 4], 5], 6])
    3
    >>> max_depth([[1, 2, [3]], 4])
    3
    >>> max_depth([1, [2, [3, [4, [5]]]]])
    5
    >>> max_depth([1, [2, 3], [4, 5]])
    2
    """
 
    
    def helper(sub_lst, current_depth):
        max = current_depth

        for i in range(len(sub_lst)):
            if isinstance(sub_lst[i], list):
                a = helper(sub_lst[i], current_depth+1)
                if a > max:
                    max = a
        return max
        # if len(sub_lst) == 0:
        #     return current_depth
        # elif isinstance(sub_lst[0], list):
            
        #     current_depth = current_depth + helper(sub_lst[0], current_depth) 
            
        #     return helper(sub_lst[1:], current_depth)
        # else:
        #     return helper(sub_lst[1:], current_depth)
            



    return helper(lst, 1) # This line should be kept and is part of the solution

