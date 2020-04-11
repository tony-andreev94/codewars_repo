# DefaultList
# https://www.codewars.com/kata/5e882048999e6c0023412908


class DefaultList:

    def __init__(self, input_list, default_value):
        self.input_list = input_list
        self.default_value = default_value

    def __getitem__(self, index):
        if -len(self.input_list) <= index < len(self.input_list):
            return self.input_list[index]
        else:
            return self.default_value

    def append(self, data):
        self.input_list.append(data)

    def extend(self, data_list):
        self.input_list.extend(data_list)

    def remove(self, element):
        del self.input_list[self.input_list.index(element)]

    def insert(self, ind, el):
        self.input_list.insert(ind, el)

    def pop(self, ind):
        self.input_list.pop(ind)


# Testing
if __name__ == "__main__":
    lst = DefaultList([1, 3, 4, 7, 2, 34], 'def')
    print(lst[10])
    lst.append('15')
    lst.extend([1, 2, 3])
    lst.remove(1)
    lst.insert(-3, 'a')
