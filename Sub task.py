nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None, ['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False, ['d', 'e', 'f', 'h', False],
	[1, 2, None, ['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None]],
	[1, 2, None]]]]

'''Задание 3*'''
'''Написать итератор аналогичный итератору из задания 1, но обрабатывающий списки с любым уровнем вложенности'''
class FlatIterator:
    def __init__(self, multi_list):
        self.multi_list = multi_list
        self.iterators_queue = []
        self.current_iterator = iter(self.multi_list)

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            try:
                self.current_element = next(self.current_iterator)
            except StopIteration:
                if not self.iterators_queue:
                    raise StopIteration
                else:
                    self.current_iterator = self.iterators_queue.pop()
                    continue
            if isinstance(self.current_element, list):
                self.iterators_queue.append(self.current_iterator)
                self.current_iterator = iter(self.current_element)
            else:
                return self.current_element


for value in FlatIterator(nested_list):
    print(value)

somelist = [value for value in FlatIterator(nested_list)]
print(somelist)

'''Задание 4*'''
'''Написать генератор аналогичный генератор из задания 2, но обрабатывающий списки с любым уровнем вложенности'''
def flatgenerator(some_list):
    for element in some_list:
        if isinstance(element, list):
            for value in flatgenerator(element):
                yield value
        else:
            yield element

print(*flatgenerator(nested_list))
