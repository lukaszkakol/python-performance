import cProfile
import memory_profiler
import sys

from examples.example_11 import (
    get_objects, get_copy, get_deep_copy,
    get_objects_with_slots, get_copy_with_slots, get_deep_copy_with_slots
)


cProfile.run('get_objects(100000)')
cProfile.run('get_objects_with_slots(100000)')
cProfile.run('get_copy(100000)')
cProfile.run('get_copy_with_slots(100000)')
cProfile.run('get_deep_copy(100000)')
cProfile.run('get_deep_copy_with_slots(100000)')

memory_profiler.profile(get_objects)(30000)
memory_profiler.profile(get_objects_with_slots)(30000)
memory_profiler.profile(get_copy)(30000)
memory_profiler.profile(get_copy_with_slots)(30000)
memory_profiler.profile(get_deep_copy)(30000)
memory_profiler.profile(get_deep_copy_with_slots)(30000)

# print(sys.getsizeof(get_objects(100000)))
# print(sys.getsizeof(get_objects_with_slots(100000)))
# print(sys.getsizeof(get_copy(100000)))
# print(sys.getsizeof(get_copy_with_slots(100000)))
# print(sys.getsizeof(get_deep_copy(100000)))
# print(sys.getsizeof(get_deep_copy_with_slots(100000)))
