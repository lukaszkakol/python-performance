import cProfile
import memory_profiler
import sys

from examples.example_9 import get_no_slots, get_slots


cProfile.run('get_no_slots(1000000)')
cProfile.run('get_slots(1000000)')

memory_profiler.profile(get_no_slots)(50000)
memory_profiler.profile(get_slots)(50000)

# print(sys.getsizeof(get_no_slots(100000)))
# print(sys.getsizeof(get_slots(100000)))
