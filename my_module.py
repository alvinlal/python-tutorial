print('importing my_module')

test = 'test string'


def find_index(list, target):
    for i, value in enumerate(list):
        if value == target:
            return i

    return -1
