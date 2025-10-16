def markdown_to_text_decorator(func):
    def wrapper(*args, **kwargs):
        #print(f"args: {args}")
        new_args = list(map(convert_md_to_txt, args))
        #print(f"new_args: {new_args}")

        #print(f"kwargs: {kwargs}")
        new_kwargs = dict(
            map(
                lambda t: (t[0], convert_md_to_txt(t[1])),
                list(kwargs.items())
            )
        )
        #print(f"new_kwargs: {new_kwargs}")
        return func(*new_args, **new_kwargs)

    return wrapper


# don't touch below this line


def convert_md_to_txt(doc):
    lines = doc.split("\n")
    for i in range(len(lines)):
        line = lines[i]
        lines[i] = line.lstrip("# ")
    return "\n".join(lines)

