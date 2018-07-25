import cProfile

from examples.example_0 import cpu_profile


cProfile.run('cpu_profile(100000)')
