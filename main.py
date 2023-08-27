from decor import logger


@logger('iterator.log')
def flat_generator(list_of_list):
    source_list = [list_of_list]
    new_list = []
    while source_list:
        val = source_list.pop(-1)
        if isinstance(val, list):
            source_list.extend(val)
        else:
            new_list.append(val)
    yield from reversed(new_list)


if __name__ == '__main__':
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    flat_generator(list_of_lists_2)
