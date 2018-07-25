import cProfile
import dis
import memory_profiler
import sys

from examples.example_5 import swap_temp, swap_tuple, test_swap


cProfile.run('test_swap(swap_temp, 1000000)')
cProfile.run('test_swap(swap_tuple, 1000000)')

# memory_profiler.profile(test_swap)(swap_temp, 100000)
# memory_profiler.profile(test_swap)(swap_tuple, 100000)

dis.dis(swap_temp)
print(); print('=' * 50); print()
dis.dis(swap_tuple)
