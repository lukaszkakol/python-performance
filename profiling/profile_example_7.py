import cProfile
import dis
import memory_profiler
import sys

from examples.example_7 import for_loop


cProfile.run('for_loop(100, 1000000)')
cProfile.run('for_loop(1000000, 100)')
cProfile.run('for_loop(10000, 10000)')

dis.dis(for_loop)
