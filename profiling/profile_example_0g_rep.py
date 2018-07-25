import cProfile
import memory_profiler
import sys

from examples.example_1 import list_comprehension


for _ in range(3):
    cProfile.run('list_comprehension(10000000)')

for _ in range(3):
    memory_profiler.profile(list_comprehension)(100000)
