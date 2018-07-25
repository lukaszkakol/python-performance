
def get_fstring(x):
    return [f'Format {i}/{x}' for i in range(x)]


def get_formatted_string(x):
    return ['Format {i}/{x}'.format(i=i, x=x) for i in range(x)]


def get_percented_string(x):
    return ['Format %(i)d/%(x)d' % {'i': i, 'x': x} for i in range(x)]
