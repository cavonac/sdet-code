import pytest


## Naive solution for fibonacci function, recursive solution
## This is not a good solution, as it is very slow for large numbers
## and it is not very memory efficient
## This is a good example of a bad solution
## Time complexity is O(2^n) and space complexity is O(n)
def fib_recursive(n: int):
    """Outputs a list of fibonacci numbers up to a given number n"""
    if n < 0:
        raise ValueError("Invalid input, must be a positive integer", n)
    
    if n <= 2:
        result = 1
    else:
        result = fib_recursive(n - 1) + fib_recursive(n - 2)
    return result


## Dynamic programming solution for fibonacci function, recursive solution
## This is a better solution, as it is faster and more memory efficient
## Time complexity is O(n) and space complexity is O(n)
def fib_dynamic(n: int, memo: dict):
    """Outputs a list of fibonacci numbers up to a given number n"""
    if n < 0:
        raise ValueError("Invalid input, must be a positive integer", n)
    
    if n in memo:
        return memo[n]
    
    if n <= 2:
        result = 1
    else:
        result = fib_dynamic(n - 1, memo) + fib_dynamic(n - 2, memo)
    memo[n] = result
    return result


## Alternative solution for returning a list of fibonacci, linear solution
def get_fibonacci_list(n: int):
    """Outputs a list of fibonacci numbers up to a given number n"""
    if n < 0:
        raise ValueError("Invalid input, must be a positive integer", n)

    a, b = 0, 1
    my_list = []
    while a <= n:
        my_list.append(a)
        a, b = b, a + b
    return my_list


def is_fibonacci(n):
    """Indicates if a given number is a fibonacci number"""
    # Quick check for negatives
    if n < 0:
        return False

    fib_list = get_fibonacci_list(n)
    if fib_list[-1] == n:
        return True
    else:
        return False


# PyTest tests
def test_fibonacci_1():
    assert get_fibonacci_list(1) == [0, 1, 1]


def test_fibonacci_9():
    assert get_fibonacci_list(9) == [0, 1, 1, 2, 3, 5, 8]


def test_fibonacci_13():
    assert get_fibonacci_list(13) == [0, 1, 1, 2, 3, 5, 8, 13]


def test_fibonacci_negative():
    with pytest.raises(ValueError):
        get_fibonacci_list(-1)


def test_is_fibonacci_0():
    assert get_fibonacci_list(0)


def test_is_fibonacci_1():
    assert is_fibonacci(1)


def test_is_fibonacci_8():
    assert is_fibonacci(8)


def test_is_fibonacci_14():
    assert is_fibonacci(14) is False


def test_is_fibonacci_negative():
    assert is_fibonacci(-1) is False


def test_fib_recursive_1():
    assert fib_recursive(1) == 1