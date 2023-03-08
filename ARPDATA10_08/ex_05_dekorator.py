import time


def timer(func):
    def wrap_func(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print(f'Function {func.__name__!r} executed in {(t2 - t1):.4f}s')
        return result

    return wrap_func

@timer
def my_long_function(n):
    variable = 0
    for i in range(100000*n):
        variable += variable + i


my_long_function(2)