import cProfile
import memory_profiler
import sys

from examples.example_4 import in_list, not_in_list, for_list, not_for_list, binary_search, not_binary_search


cProfile.run('in_list(10000)')
cProfile.run('not_in_list(10000)')
cProfile.run('for_list(10000)')
cProfile.run('not_for_list(10000)')
cProfile.run('binary_search(10000)')
cProfile.run('not_binary_search(10000)')

# memory_profiler.profile(in_list)(10000)
# memory_profiler.profile(not_in_list)(10000)
# memory_profiler.profile(for_list)(10000)
# memory_profiler.profile(not_for_list)(10000)
