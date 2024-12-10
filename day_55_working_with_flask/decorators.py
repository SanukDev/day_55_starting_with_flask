def h1_tag(func):
    def another_func(*args, **kwargs):
        return f"<h1>{func()}</h1>"
    return another_func