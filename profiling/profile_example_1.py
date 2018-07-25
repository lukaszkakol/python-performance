import cProfile
import memory_profiler
import sys

from examples.example_1 import list_comprehension, list_append, list_extend


cProfile.run('list_comprehension(1000000)')
cProfile.run('list_append(1000000)')
cProfile.run('list_extend(1000000)')

# memory_profiler.profile(list_comprehension)(100000)
# memory_profiler.profile(list_append)(100000)
# memory_profiler.profile(list_extend)(100000)
