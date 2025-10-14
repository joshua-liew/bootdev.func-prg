def doc_format_checker_and_converter(conversion_function, valid_formats):
    def convert(filename, content):
        format = filename.split(".")[-1]
        if format in valid_formats:
            return conversion_function(content)
        raise ValueError(f"invalid file format")
    return convert


# Don't edit below this line


def capitalize_content(content):
    return content.upper()


def reverse_content(content):
    return content[::-1]

