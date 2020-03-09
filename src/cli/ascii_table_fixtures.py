import random


def typeSamples(type):
    if type == 'boolean':
        list1 = [True, False]
        return random.sample(list1, len(list1))

    if type == 'char':
        list1 = ['a', 'b', 'c']
        return random.sample(list1, len(list1))

    if type == 'float':
        list1 = [12312.21, 235.98, 45.8]
        return random.sample(list1, len(list1))

    if type == 'integer':
        list1 = [5]
        return random.sample(list1, len(list1))

    if type == 'timestamp:sequence':
        list1 = ['1994-02-20 18:48:33',
                 '1994-02-20 18:48:34',
                 ]
        return random.sample(list1, len(list1))

    if type == 'integer:sequence':
        list1 = [1, 2, 3, 4, 5]
        return list1

    if type == 'string':
        list1 = ['KJZWEqsMnUZCnIo',
                 'QyksAoTESCkDdiT',
                 'leuvVpOMCffDmpl',
                 'iOdCxyBunDGlyBP',
                 'RemSUYMSuPNUibT',
                 'csXdrjehwcNwhrV',
                 'nnLQoOWGkJipUpD',
                 'ogmoZkWnhkqIQfb',
                 'DbLLOuiKTRFvXsC',
                 'gqltfyuhyeRUANb']
        return random.sample(list1, 2)

    if type == 'timestamp':
        list1 = ['2000-07-28 09:03:58',
                 '2006-11-10 05:29:55',
                 '2001-12-02 23:54:50',
                 '2010-06-26 22:16:58',
                 '1994-11-11 17:52:57',
                 ]
        return random.sample(list1, 2)
