import copy


"""
MyClass(
    x = MyClass(
        x = object()
    )
)
"""


class MyClass(object):

    def __init__(self, nested=True):
        if nested:
            self.x = MyClass(False)
        else:
            self.x = object()


class MyClassWithSlots(object):

    __slots__ = ['x']

    def __init__(self, nested=True):
        if nested:
            self.x = MyClass(False)
        else:
            self.x = object()


def get_objects(x):
    result = [MyClass() for _ in range(x)]
    return result


def get_objects_with_slots(x):
    result = [MyClassWithSlots() for _ in range(x)]
    return result


def get_copy(x):
    result = [MyClass() for _ in range(x)]
    copied_result = [copy.copy(obj) for obj in result]
    return copied_result


def get_copy_with_slots(x):
    result = [MyClassWithSlots() for _ in range(x)]
    copied_result = [copy.copy(obj) for obj in result]
    return copied_result


def get_deep_copy(x):
    result = [MyClass() for _ in range(x)]
    deep_copied_result = [copy.deepcopy(obj) for obj in result]
    return deep_copied_result


def get_deep_copy_with_slots(x):
    result = [MyClassWithSlots() for _ in range(x)]
    deep_copied_result = [copy.deepcopy(obj) for obj in result]
    return deep_copied_result
