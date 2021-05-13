from collections import Counter


def counter_method():
    lst = ['abc', 'for', 'tech', 'tech', 'abc', 'for', 'abc', 'tech', 'abc', 'for']
    d = {'a': 1, 'b': 2}
    t1 = Counter('abccbaabbcabccaab')
    t2 = Counter({'a': 3, 'b': 5, 'c': -8, 'd': 0})
    t3 = Counter(a=5, b=8, c=9)
    t4 = ({'a': 7, 'b': 2, 'c': -3, 'd': 1})
    t5 = Counter([1, 2, 3])
    t6 = Counter([3, 2, 1, 1, 2, 3])

    toll = Counter(lst)

    print(toll)
    print(toll['abc'])
    print(toll['for'])
    print(toll['tech'])
    print(d['a'])
    print(d['b'])
    print(list(t1.elements()))
    print(list(t2.elements()))
    print(t1.most_common(1))
    print(t1.most_common(2))
    print(t1.most_common(3))
    print(t3.subtract(t4))
    print(t3.keys())
    print(t3.values())
    print(t3.items())
    t2.clear()
    print(t2)
    print(t5 + t6)
    print(t5 - t6)
    print(t5 | t6)
    print(t5 & t6)


if __name__ == "__main__":
    counter_method()
