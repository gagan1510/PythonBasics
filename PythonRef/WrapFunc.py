from functools import wraps

def trace_in(func, *args, **kwargs):
    print("Entering function", func.__name__)

def trace_out(func, *args, **kwargs):
    # print("Leaving function", func.__name__)
    try:
        print("Leaving function", func.__name__)
    except TypeError:
        pass


@trace_out
def calc(x, y):
    # return x+y
    print("The sum is ", x + y)


try:
    print(calc(1, 2))
except TypeError:
    print("TypeError")