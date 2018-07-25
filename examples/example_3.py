
def iterate_indexes(x):
    list_a = [i for i in range(x)]
    list_b = [str(a) for a in list_a]

    for idx in range(x):
        x = list_a[idx]
        y = list_b[idx]


def zip_lists(x):
    list_a = [i for i in range(x)]
    list_b = [str(a) for a in list_a]

    for x, y in zip(list_a, list_b):
        pass


def dictionary(x):
    my_dict = {i: str(i) for i in range(x)}

    for x, y in my_dict.items():
        pass
