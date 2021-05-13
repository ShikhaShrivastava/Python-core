'''_____________Counter Object_________________'''
from collections import Counter


def counter_object_demo():
    lst = ['a', 'b', 'c', 'b', 'a', 'c', 'a', 'c', 'b']
    tup = (1, 2, 3, 2, 1, 4, 2, 3, 1, 2, 1, 3, 2)
    set_ele = {10, 30, 20, 10, 20, 40, 60, 10}
    dct = {'a': 1, 'b': 5, 'c': 9, 'd': 8}
    data = 'hey there is whatsapp'
    toll_lst = Counter(lst)
    toll_tup = Counter(tup)
    toll_set = Counter(set_ele)
    toll_dict1 = Counter(dct)
    toll_data = Counter(data)
    toll_dict2 = Counter(a=2, b=3, c=5)

    print(toll_lst)
    print(toll_tup)
    print(toll_set)
    print(toll_dict1)
    print(toll_dict2)
    print(toll_data)


if __name__ == "__main__":
    counter_object_demo()
