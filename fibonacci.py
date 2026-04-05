# Fibonacci Sequence Implementation
# Recursive and Iterative Approaches

# Recursive Function
def fibonacci_recursive(n):
    """
    Recursive implementation of Fibonacci
    Base cases:
    F(0) = 0
    F(1) = 1
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


# Iterative Function
def fibonacci_iterative(n):
    """
    Iterative implementation of Fibonacci
    More efficient than recursion
    """
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


# Example Test
if __name__ == "__main__":
    n = 5

    print("Recursive Result:", fibonacci_recursive(n))
    print("Iterative Result:", fibonacci_iterative(n))
