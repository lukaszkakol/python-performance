import timeit

from examples.example_0 import cpu_profile


print(timeit.timeit('cpu_profile(100000)', 'from examples.example_0 import cpu_profile', number=100))
