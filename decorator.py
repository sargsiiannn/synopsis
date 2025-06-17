# Wraps a function and changes its output to uppercase
# Adds behavior without modifying original function

def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@uppercase_decorator
def say_hello():
    return "hello there"

print(say_hello())  # HELLO THERE
