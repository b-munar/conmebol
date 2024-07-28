def set_if_not_none(dictionary_map, key, value):
    if (value is not None  and value) or (type(value)==bool or (value==0)):
        dictionary_map[key] = value