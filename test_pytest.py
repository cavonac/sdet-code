def fibo(n):
    # Outputs a list of numbers up to and including the given number: n (if n is a fibonacci number)
    a, b = 0, 1
    list = []
    while a <= n:
        list.append(a)
        a, b = b, a+b
    return list

def test_fibo_1():
    assert fibo(1) == [0, 1, 1]

def test_fibo_10():
    assert fibo(10) == [0, 1, 1, 2, 3, 5, 8]

def test_fibo_9():
    assert fibo(9) == [0, 1, 1, 2, 3, 5, 8]

def test_fibo_13():
    assert fibo(13) == [0, 1, 1, 2, 3, 5, 8, 13]

