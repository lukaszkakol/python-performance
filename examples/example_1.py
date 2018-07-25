
def list_comprehension(x):
    result = [i*i for i in range(x)]
    return result


def list_append(x):
    result = []
    for i in range(x):
        result.append(i*i)
    return result


def list_extend(x):
    result = []
    result.extend(i*i for i in range(x))
    return result
