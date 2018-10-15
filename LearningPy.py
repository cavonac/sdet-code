def fibonacci(n):
    """ Outputs a list of numbers up to and including the given number (if it is a fibonacci number) """
    a, b = 0, 1
    my_list = []
    while a <= n:
        my_list.append(a)
        a, b = b, a + b
    return my_list


def is_fibonacci(n):
    """ Indicates if the number given is a fibonacci number """
    fib_list = fibonacci(n)
    if fib_list[-1] == n:
        return True
    else:
        return False


def test_fibonacci_1():
    assert fibonacci(1) == [0, 1, 1]


def test_fibonacci_9():
    assert fibonacci(9) == [0, 1, 1, 2, 3, 5, 8]


def test_fibonacci_13():
    assert fibonacci(13) == [0, 1, 1, 2, 3, 5, 8, 13]


def test_is_fibonacci_0():
    assert fibonacci(0)


def test_is_fibonacci_1():
    assert is_fibonacci(1)


def test_is_fibonacci_8():
    assert is_fibonacci(8)


def test_is_fibonacci_14():
    assert is_fibonacci(14) is False
