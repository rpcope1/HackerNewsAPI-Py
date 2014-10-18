__author__ = 'Robert P. Cope'
from functools import wraps
import time


#TODO: Does this need thread safety?
def rate_limit(wait_time=10):
    wait_time /= 1000.0  # Convert from ms to s.

    def wrapper(func):
        last_call = [0.0]

        @wraps(func)
        def rate_limited_func(*args, **kwargs):
            time_elapsed = time.clock() - last_call[0]
            if time_elapsed < wait_time:
                time.sleep(wait_time - time_elapsed)
            ret_val = func(*args, **kwargs)
            last_call[0] = time.clock()
            return ret_val

        return rate_limited_func

    return wrapper