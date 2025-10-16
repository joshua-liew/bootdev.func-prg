def args_logger(*args, **kwargs):
    for i in range(len(args)):
        print(f"{i+1}. {str(args[i])}")

    kwargs_keys_sorted = sorted(kwargs.items(), key=lambda t: t[0])
    for k in kwargs_keys_sorted:
        print(f"* {k[0]}: {k[1]}")
