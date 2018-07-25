
def check_in(elem, list_):
    return elem in list_


def check_for(elem, list_):
    for element in list_:
        if element == elem:
            return True
    else:
        return False


def check_binary(elem, list_):
    start = 0
    end = len(list_) - 1
    while start < end:
        mid = (start + end) // 2
        if elem < list_[mid]:
            end = mid - 1
        elif elem > list_[mid]:
            start = mid + 1
        else:    # elem == list_[mid]
            return True

    return False


def in_list(x):
    my_list = [i for i in range(x)]

    for i in range(x):
        check_in(i, my_list)


def not_in_list(x):
    my_list = [i for i in range(x)]

    for i in range(x, 2*x):
        check_in(i, my_list)


def for_list(x):
    my_list = [i for i in range(x)]

    for i in range(x):
        check_for(i, my_list)


def not_for_list(x):
    my_list = [i for i in range(x)]

    for i in range(x, 2*x):
        check_for(i, my_list)


def binary_search(x):
    my_list = [i for i in range(x)]

    for i in range(x):
        check_binary(i, my_list)


def not_binary_search(x):
    my_list = [i for i in range(x)]

    for i in range(x, 2*x):
        check_binary(i, my_list)
