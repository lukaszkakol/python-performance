GLOBAL_CONST = 10000000


def global_func():
    for i in range(GLOBAL_CONST):
        res = GLOBAL_CONST + i


def parametrized_func(x):
    for i in range(x):
        res = x + i
