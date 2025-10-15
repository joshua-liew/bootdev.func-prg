def word_count_aggregator():
    count = 0

    def get_number_of_words(doc):
        nonlocal count
        count += len(doc.split())
        return count

    return get_number_of_words
