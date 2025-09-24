from collections import ChainMap

def chain_map_example():
    dict_1 = {"one": 1, "two": 2}
    dict_2 = {"three": 3, "four": 4}

    chain_map = ChainMap(dict_1, dict_2)

    print(chain_map)