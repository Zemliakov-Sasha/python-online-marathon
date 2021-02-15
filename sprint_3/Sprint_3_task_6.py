import random
def randomWord(lst):
    l = list(range(len(lst)))
    if len(lst) == 0:
        yield None
    else:
        random.shuffle(l)
        for i in l:
            yield lst[i]
        i = 0
        while True:
            if i == len(lst):
                i = 0
            yield lst[i]
            i += 1





list1 = ['book', 'apple', 'word']

books = randomWord(list1)
print(next(books))
print(next(books))
print(next(books))
print(next(books))
print(next(books))
print(next(books))
print(next(books))
print(next(books))
print(next(books))