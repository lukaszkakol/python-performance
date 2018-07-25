import cProfile

from examples.example_0 import memory_profile


cProfile.run('memory_profile(50000)')
