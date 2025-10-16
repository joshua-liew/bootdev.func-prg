def configure_plugin_decorator(func):
    def wrapper(*args):
        new_dict = dict(args)
        return func(**new_dict)
    return wrapper
