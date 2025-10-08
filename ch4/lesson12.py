def list_files(parent_directory, current_filepath=""):
    filepaths = []
    
    for (key, value) in parent_directory.items():
        if value is None:
            filepaths.append(current_filepath + f"/{key}")
        else:
            filepaths.extend(list_files(value, current_filepath + f"/{key}"))

    return filepaths
