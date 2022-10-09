import time
from functools import wraps


def decorator_with_no_arguments(f):
    print("decorator called")
    @wraps(f)
    def wrapper(*args, **kwargs):
        print(f"Will run function {f.__name__}")
        result = f(*args, **kwargs)
        print(f"Finished running function {f.__name__}")
        return result

    return wrapper


def decorator_with_arguments(time_it: bool):
    print("decorator_with_arguments called")
    def decorator(f):
        print("decorator called")
        @wraps(f)
        def wrapper(*args, **kwargs):
            print(f"Will run function {f.__name__}")
            if time_it:
                start_time = time.perf_counter()

            result = f(*args, **kwargs)

            if time_it:
                elapsed_time = time.perf_counter() - start_time
                print(f"function took: {elapsed_time}")

            print(f"Finished running function {f.__name__}")
            return result
        return wrapper
    return decorator


@decorator_with_no_arguments
def func(arg1: str):
    """ some function """
    print(f"running func with: {arg1=}")


# @decorator_with_arguments(True)
def multiply(x: int, y: int) -> int:
    """ Multiplies two values """
    print(f"multiplying {x} by {y}")
    return x * y
# (.venv) PS C:\Users\Piotr\Repos\Python> python .\python\lesson_4\decorators.py
# decorator called
# Will run function func
# running func
# Finished running function func


# (.venv) PS C:\Users\Piotr\Repos\Python> python .\python\lesson_4\decorators.py
# decorator called
# decorator_with_arguments called
# decorator called
# Will run function multiply
# multiplying 1 by 5
# function took: 0.0005969000048935413
# Finished running function multiply

if __name__ == "__main__":
    # func("argument1")
    # multiply(1, 5)
    func = decorator_with_no_arguments(multiply)
    print(func.__name__)
    print(func.__doc__)
    # func(8, 5)
    
    decorator_with_time_it = decorator_with_arguments(True)
    multi_wrapper = decorator_with_time_it(multiply)

    print(multi_wrapper.__name__)
    print(multi_wrapper.__doc__)
    # multi = multi_wrapper(8, 5)

    # multi2 = decorator_with_arguments(True)(multiply)(8, 5)
    
    # multi == multi2
    # print(multi)
    # print(multi2)
