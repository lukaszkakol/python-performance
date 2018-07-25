import cProfile
import memory_profiler
import sys

from examples.example_3 import iterate_indexes, zip_lists, dictionary


cProfile.run('iterate_indexes(1000000)')
cProfile.run('zip_lists(1000000)')
cProfile.run('dictionary(1000000)')

# memory_profiler.profile(iterate_indexes)(10000)
# memory_profiler.profile(zip_lists)(10000)
# memory_profiler.profile(dictionary)(10000)
