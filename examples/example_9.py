
class MyClassNoSlots(object):

    def __init__(self):
        self.x = object()


class MyClassWithSlots(object):

    __slots__ = ['x']

    def __init__(self):
        self.x = object()


def get_no_slots(x):
    result = [MyClassNoSlots() for _ in range(x)]
    return result


def get_slots(x):
    result = [MyClassWithSlots() for _ in range(x)]
    return result
