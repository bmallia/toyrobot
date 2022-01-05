
def coroutine_decorator(func):
    def wrap(*args, **kwargs):
        obj = func(*args, **kwargs)
        obj.__next__()
        return obj
    return wrap