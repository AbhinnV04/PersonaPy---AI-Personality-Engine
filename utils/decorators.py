"""
# src/utils/decorators.py
========================
This module contains decorators for various purposes in the package.
- core_function: Marks a function as a core package endpoint.
- internal_test: Marks a function as an internal test function.
- endpoint: Marks a function as an endpoint for the package.
"""
import functools

def core_function(func):
    """Decorator to indicate that this function is a core package endpoint."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[CORE FUNCTION] Running {func.__name__}()")
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

def endpoint(func):
    """ Decorator to indicate that the function serves as an endpoint. """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[ENDPOINT FUNCTION] Running {func.__name__}()")
        print("--"*30)
        return func(*args, **kwargs)
    return wrapper