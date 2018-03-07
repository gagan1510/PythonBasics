class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
          pass
    #     for i in iterable:
    #         self.items_list.append(i)

    __update = update

class MappingSubclass(Mapping):
    def update(self, keys, values):
        for item in zip(keys, values):
            self.items_list.append(item)

l = [1, 2, 3, 4]
v = ['gagan', 'preet', 'singh', 'kainth']
a = MappingSubclass(l)
a.update(l, v)
print(a.items_list)