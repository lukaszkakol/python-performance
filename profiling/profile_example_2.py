import cProfile
import memory_profiler
import sys

from examples.example_2 import get_tuple, get_list, get_set, get_dict


cProfile.run('get_tuple(1000000)')
cProfile.run('get_list(1000000)')
cProfile.run('get_set(1000000)')
cProfile.run('get_dict(1000000)')

# memory_profiler.profile(get_tuple)(100000)
# memory_profiler.profile(get_list)(100000)
# memory_profiler.profile(get_set)(100000)
# memory_profiler.profile(get_dict)(100000)

print(sys.getsizeof(get_tuple(1000000)))
print(sys.getsizeof(get_list(1000000)))
print(sys.getsizeof(get_set(1000000)))
print(sys.getsizeof(get_dict(1000000)))
