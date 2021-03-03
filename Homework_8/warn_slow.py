import time
import sys

def warn_slow(func):
    def inner(*args, **kwargs):
        start = time.time()
        result = func(*args)
        duration = time.time() - start
        if duration > 2:
            print(f'It took {duration} seconds, {func.__name__} function arguments are --> {args}')
        return result
    return inner

@warn_slow
def func_slow(n):
    time.sleep(3)
    result = ' *'
    for i in range(n):
        print('  ' * (n - i - 1) + result * (i + 1), end='')
        print('')
    for i in range(n - 1):
        print('  ' * (i + 1) + result * (n - i - 1), end=' ')
        print('')



@warn_slow
def func_fast(x, y, z):
    s = x*y
    print(f'Result of func_fast function is {s}')

func_slow(5)
print()
func_fast(10, 15, 20)

