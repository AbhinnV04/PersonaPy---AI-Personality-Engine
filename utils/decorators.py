import functools

def core_function(func):
    """Decorator to indicate that this function is a core package endpoint."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # print(f"[CORE FUNCTION] Running {func.__name__}()")
        return func(*args, **kwargs)
    return wrapper

def internal_test(func):
    """Decorator to indicate that this function is for internal testing only."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[INTERNAL TEST] Running {func.__name__}()")
        print("--"*30)
        return func(*args, **kwargs)
    return wrapper
