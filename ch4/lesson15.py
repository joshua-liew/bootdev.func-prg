def count_nested_levels(nested_documents, target_document_id, level=1):
    result = -1

    for key in nested_documents.keys():
        if key == target_document_id:
            result = level
        else:
            result = count_nested_levels(
                nested_documents[key],
                target_document_id,
                (level + 1)
            )

        if result != -1:
            return result
    
    return result
