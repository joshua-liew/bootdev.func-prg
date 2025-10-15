def create_markdown_image(alt_text):
    img_syntax = f"![{alt_text}]"

    def append_url(url):
        url = url.replace("(", "%28").replace(")", "%29")
        nonlocal img_syntax
        img_syntax += f"({url})"

        def append_title(title=None):
            nonlocal img_syntax
            if title:
                title = f"\"{title}\""
                img_syntax = img_syntax[:-1] + f" {title})"
            return img_syntax

        return append_title

    return append_url
