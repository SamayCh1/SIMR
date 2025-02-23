
# Exercise 1
def make_subsets(lst):
    """
    Find all subsets of a given list.

    A subset is any combination of elements from the original list, including the empty set and the list itself.

    Parameters:
    - lst (list): The list from which to find subsets.

    Returns:
    - list of lists: A list containing all subsets of the original list.

    Examples:
    >>> make_subsets([])
    [[]]
    >>> make_subsets([1])
    [[], [1]]
    >>> make_subsets([1, 2])
    [[], [1], [2], [1, 2]]
    >>> make_subsets([1, 2, 3])
    [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    >>> make_subsets(["a", "b", "c", "d"])  # Example provided
    [[], ['a'], ['b'], ['a', 'b'], ['c'], ['a', 'c'], ['b', 'c'], ['a', 'b', 'c'], ['d'], ['a', 'd'], ['b', 'd'], ['a', 'b', 'd'], ['c', 'd'], ['a', 'c', 'd'], ['b', 'c', 'd'], ['a', 'b', 'c', 'd']]
    """
    
    if lst == []:
        return [[]]
    subs = make_subsets(lst[:-1])
    return subs + [item + [lst[-1]] for item in subs] 
    


# Exercise 2
def fibonacci(n):
    """
    Calculate the n-th Fibonacci number using tree recursion with memoization.

    Memoization is an optimization technique that stores the results of expensive function calls
    and reuses them when the same inputs occur again.

    Parameters:
    - n (int): The position in the Fibonacci sequence.

    Returns:
    - int: The n-th Fibonacci number.

    Examples:
    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(2)
    1
    >>> fibonacci(5)
    5
    >>> fibonacci(10)  # Example provided
    55
    >>> fibonacci(30)  # Example provided
    832040
    """
    def helper(n, memo):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n in memo: 
            return memo[n] 
        else:
            memo[n] = helper(n-1, memo) + helper(n-2, memo)
            print(memo)
            return memo[n]
        
    return helper(n, {})

print(fibonacci(5))

class KTreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

# Exercise 3
def find_height(node):
    """
    Find the height of a k-ary tree using tree recursion.

    The height of a tree is the number of edges from the root to the furthest leaf node.

    Parameters:
    - node (KTreeNode): The root node of the tree.

    Returns:
    - int: The height of the tree.

    Examples:
    >>> root = KTreeNode(1)
    >>> find_height(root)
    0
    >>> child1 = KTreeNode(2)
    >>> root.children.append(child1)
    >>> find_height(root)
    1
    >>> child2 = KTreeNode(3)
    >>> root.children.append(child2)
    >>> child3 = KTreeNode(4)
    >>> child1.children.append(child3)
    >>> find_height(root)
    2
    >>> child4 = KTreeNode(5)
    >>> child3.children.append(child4)
    >>> find_height(root)  # Example provided
    3
    """
    # if len(node.children) == 0:
    #     return -1
    # heights = []
    # for child in node.children:
    #     heights.append(find_height(child))

    # return max(heights)
    
    if not node or not node.children:
        return 0
    else:
        return 1 + max(find_height(child) for child in node.children)

    # if len(node.children) == 1: 
    #     return 1
    # max = 0
    # level = 0
    # for child in node.children:
    #     # if len(node.children) > 1:
    #     level +=1     
    #     # if level >= max:
    #     #     max = level
    #     level += find_height(child)
    # return level
        



