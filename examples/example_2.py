
def get_tuple(x):
    result = tuple(i for i in range(x))
    return result


def get_list(x):
    result = [i for i in range(x)]
    return result


def get_set(x):
    result = {i for i in range(x)}
    return result


def get_dict(x):
    result = {i: str(i) for i in range(x)}
    return result
