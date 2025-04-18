from time import time


def timer_it(func):
    # This function shows the execution time of
    # the function object passed
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2 - t1):.4f}s')
        return result

    return wrap_func


@timer_it
def factorial(n):
    return 1 if n in (0, 1) else n * factorial(n - 1)

print(factorial(52))

