import cProfile
import memory_profiler
import sys

from examples.example_6 import get_fstring, get_formatted_string, get_percented_string


cProfile.run('get_fstring(1000000)')
cProfile.run('get_formatted_string(1000000)')
cProfile.run('get_percented_string(1000000)')

# memory_profiler.profile(get_fstring)(100000)
# memory_profiler.profile(get_formatted_string)(100000)
# memory_profiler.profile(get_percented_string)(100000)

print(sys.getsizeof(get_fstring(1000000)))
print(sys.getsizeof(get_formatted_string(1000000)))
print(sys.getsizeof(get_percented_string(1000000)))
