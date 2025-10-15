def new_collection(initial_docs):
    docs = initial_docs.copy()

    def append_to_collection(string):
        docs.append(string)
        return docs

    return append_to_collection
