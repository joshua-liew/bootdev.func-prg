from functools import reduce


def lines_with_sequence(char):
    def with_char(length):
        sequence = char * length

        def with_length(doc):
            lines = doc.splitlines()
            count = reduce(
                lambda x, y: (x + 1) if sequence in y else (x + 0),
                lines,
                0
            )
            return count

        return with_length

    return with_char

