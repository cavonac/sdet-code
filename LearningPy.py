def fibonacci(n):
    # Outputs a list of numbers up to and including the given number (if n is a fibonacci number)
    a, b = 0, 1
    my_list = []
    while a <= n:
        my_list.append(a)
        a, b = b, a + b
    return my_list


def test_fibonacci_1():
    assert fibonacci(1) == [0, 1, 1]


def test_fibonacci_10():
    assert fibonacci(10) == [0, 1, 1, 2, 3, 5, 8]


def test_fibonacci_9():
    assert fibonacci(9) == [0, 1, 1, 2, 3, 5, 8]


def test_fibonacci_13():
    assert fibonacci(13) == [0, 1, 1, 2, 3, 5, 8, 13]
