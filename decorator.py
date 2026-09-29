import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Before Execution")
        before_time = time.time()
        result = func(*args, **kwargs)
        after_time = time.time()
        print(f"After execution - Total Time #{after_time - before_time}")
        return result
    return wrapper

@timer # ---- slow_func = timer(slow_func)
def slow_func():
    print("In slow func")
    time.sleep(1)

@timer
def mul(a, b):
    return a * b

#tr = timer(slow_func)
slow_func()
print(mul(2,3))
print(mul.__name__)