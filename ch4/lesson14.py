def find_longest_word(document, longest_word=""):
    if document == " ":
        return longest_word

    if " " in document:
        first_word, document = document.split(maxsplit=1)
        longest_word = find_longest_word(document, longest_word)
    else:
        first_word, document = document, None

    if len(first_word) >= len(longest_word):
        longest_word = first_word
    return longest_word
