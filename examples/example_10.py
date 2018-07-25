import copy


def copy_list_constructor(x):
    original = [i for i in range(x)]
    result = list(original)
    return result


def copy_list_comprehension(x):
    original = [i for i in range(x)]
    result = [a for a in original]
    return result


def copy_list_slice(x):
    original = [i for i in range(x)]
    result = original[:]
    return result


def copy_list_copy(x):
    original = [i for i in range(x)]
    result = copy.copy(original)
    return result


def copy_list_deep_copy(x):
    original = [i for i in range(x)]
    result = copy.deepcopy(original)
    return result
