def zipmap(keys, values):
    zip_dict = {}
    if not keys or not values:
        return zip_dict
    zip_dict[keys[0]] = values[0]
    return zip_dict | zipmap(keys[1:], values[1:])
