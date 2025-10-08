def sum_nested_list(lst):
    if len(lst) == 0:
        return 0
    if type(lst[0]) is list:
        return sum_nested_list(lst[0]) + sum_nested_list(lst[1:])

    return lst[0] + sum_nested_list(lst[1:])
