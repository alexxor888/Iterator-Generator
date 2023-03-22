class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.counter = -1
        return self


    def __next__(self):
        self.counter += 1
        flat_list = []
        for x in self.list_of_list:
            for el in x:
                flat_list.append(el)
        if self.counter == len(self.list_of_list):
            raise StopIteration
        item = self.list_of_list[self.counter]
        print(flat_list)
        return item

flat_iterator = FlatIterator(list_of_list=[['a', 'b', 'c'],['d', 'e', 'f', 'h', False],[1, 2, None]])


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()