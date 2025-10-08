def sum_nested_list(lst):
    if len(lst) == 0:
        return 0

    if type(lst[0]) is list:
        val = sum_nested_list(lst[0])
    else:
        val = lst[0]
    return val + sum_nested_list(lst[1:])
