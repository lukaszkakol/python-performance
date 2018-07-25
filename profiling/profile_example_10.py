import cProfile
import memory_profiler
import sys

from examples.example_10 import (
    copy_list_constructor, copy_list_comprehension, copy_list_slice,
    copy_list_copy, copy_list_deep_copy
)


cProfile.run('copy_list_constructor(10000000)')
cProfile.run('copy_list_comprehension(10000000)')
cProfile.run('copy_list_slice(10000000)')
cProfile.run('copy_list_copy(10000000)')
cProfile.run('copy_list_deep_copy(10000000)')

# memory_profiler.profile(copy_list_constructor)(1000000)
# memory_profiler.profile(copy_list_comprehension)(1000000)
# memory_profiler.profile(copy_list_slice)(1000000)
# memory_profiler.profile(copy_list_copy)(1000000)
# memory_profiler.profile(copy_list_deep_copy)(100000)

# print(sys.getsizeof(copy_list_constructor(10000000)))
# print(sys.getsizeof(copy_list_comprehension(10000000)))
# print(sys.getsizeof(copy_list_slice(10000000)))
# print(sys.getsizeof(copy_list_copy(10000000)))
# print(sys.getsizeof(copy_list_deep_copy(10000000)))
