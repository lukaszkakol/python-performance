import cProfile
import dis

from examples.example_8 import global_func, parametrized_func


cProfile.run('global_func()')
cProfile.run('parametrized_func(10000000)')

dis.dis(global_func)
print()
print('='*80)
print()
dis.dis(parametrized_func)
