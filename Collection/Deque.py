from collections import deque


def creating_deque():
    deck1 = deque([10, 20, 30, 40, 50])
    print(deck1)
    print(type(deck1))
    deck2 = deque('abc for tech')
    print(deck2)
    print(type(deck2))


if __name__ == "__main__":
    creating_deque()

'''appending & accessing deque'''
print("")
print("appending & accessing deque")


def appending_deque():
    deck1 = deque([10, 20, 30, 40, 50])
    print("")
    print("appending:")
    print(deck1)
    deck1.append(60)
    print(deck1)
    deck1.appendleft(5)
    print(deck1)
    print(deck1[-2])

    print("")
    print("extend:")
    lst = [45, 55, 65]
    deck1.extend(lst)
    print(deck1)
    lst1 = [1, 2, 3, 4]
    deck1.extendleft(lst1)
    print(deck1)

    print("")
    print("pop")
    print(deck1.pop())
    print(deck1.popleft())

    print("")
    print("insert")
    deck1.insert(3, 72)
    print(deck1)

    print("")
    print("remove")
    deck1.remove(40)
    print(deck1)

    print("")
    print("reverse")
    deck1.reverse()
    print(deck1)

    print("")
    print("copy,clear,count")
    deck2 = deck1.copy()
    print(deck2)
    deck2.clear()
    print(deck2)
    print(deck1.count(1))

    print("")
    print("rotate")
    fruits = deque(["apple", "mango", "banana", "kiwi", "pineapple"])
    fruits.rotate(2)
    print(fruits)
    fruits.rotate(-3)
    print(fruits)


if __name__ == "__main__":
    appending_deque()