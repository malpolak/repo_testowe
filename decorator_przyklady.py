from functools import wraps
import time


def dekorator(func):
    @wraps(func)
    def opakowanie(*args, **kwargs):
        print("Coś przed oryginalną funckja")

        r = func(*args, **kwargs)

        print("Coś po oryginalnej funkcji")

        return r

    return opakowanie


def timeit(func):
    @wraps(func)
    def opakowanie(*args, **kwargs):
        t = time.time()

        r = func(*args, **kwargs)

        print(f"Wykonanie funkcji  {func.__name__} zajelo {time.time() - t}s")

        return r

    return opakowanie

    ...


@timeit
def hello_world():
    return "Hello World"


@dekorator
def hello(name):
    """Dokumentacja naszej funkcji"""
    return f"Hello {name}"


hello_world = dekorator(hello_world)
hello_world()

hello = dekorator(hello)

hello("Rafał")

print("a")
