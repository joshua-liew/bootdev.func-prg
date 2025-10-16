from functools import lru_cache


@lru_cache
def is_palindrome(word):
    #print(word)
    if len(word) <= 1:
        return True

    first_letter, last_letter = word[0], word[-1]
    if first_letter == last_letter:
        return is_palindrome(word[1:-1])

    return False
