def fibo(n):
    a, b = 0, 1
    list = []
    while a < n:
        list.append(a)
        a, b = b, a+b
    return list

def test_fibo_1():
    assert fibo(1) == [0]

def test_fibo_10():
    assert fibo(10) == [0, 1, 1, 2, 3, 5, 8]