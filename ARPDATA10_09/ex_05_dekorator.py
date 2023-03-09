import time


def timer(func):
    def wrap_func(*args, **kwargs):
        t1 = time.time()
        print("Jeszcze nie wykonuje funkcji")
        result = func(*args, **kwargs)
        print("wykonalem funkcje")

        t2 = time.time()

        print(
            f"Function {func.__name__} executed in {(t2 - t1):.4f}"
        )
        return result

    return wrap_func


@timer
def my_long_function(n):
    variable = 0
    print("jestem w funkcji")
    for i in range(100000 * n):
        variable += variable + i


my_long_function(2)
