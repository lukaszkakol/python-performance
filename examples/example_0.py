import memory_profiler


def cpu_profile(x):
    list_a = [i for i in range(x)]
    list_b = [i for i in range(x, 2*x)]
    del list_a
    return list_b


@memory_profiler.profile(precision=4)
def memory_profile(x):
    list_a = [i for i in range(x)]
    list_b = [i for i in range(x, 2*x)]
    del list_a
    return list_b


def gcd(x, y):
    while y:
        temp = x % y
        x = y
        y = temp
    return x
