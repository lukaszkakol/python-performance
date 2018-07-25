
def swap_temp(x, y):
    temp = x
    x = y
    y = temp


def swap_tuple(x, y):
    x, y = y, x


def test_swap(func, n):
    for _ in range(n):
        a = object()
        b = object()
        func(a, b)
