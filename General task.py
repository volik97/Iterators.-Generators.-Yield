nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

'''Задание 1'''
'''Написать итератор, который принимает список списков, и возвращает их плоское представление, т.е последовательность состоящую из вложенных элементов'''
class FlatIterator:
    def __init__(self, object):
        self.object = sum(object, [])

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.object):
            raise StopIteration
        else:
            return self.object[self.index]


nested_iter = FlatIterator(nested_list)

for value in nested_iter:
    print(value)

flat_list = [item for item in nested_iter]
print(flat_list)

'''Задание 2'''
'''Написать генератор'''

def flat_generator(my_list):
    for lists in my_list:
        for item in lists:
            yield item

print(*flat_generator(nested_list))