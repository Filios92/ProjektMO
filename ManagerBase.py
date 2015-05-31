# Manager base
class ManagerBase:
    """docstring for ManagerBase"""
    def __init__(self):
        self._array = []

    def add(self, element):
        self.get_next_index_for_array(element)
        self._array.append(element)
        return element.index

    @property
    def size(self):
        return len(self._array)

    def get_list(self):
        return self._array

    def get(self, index):
        return self._array[index]

    def get_index(self, element):
        return self._array.index(element)

    def get_next_index_for_array(self, element):
        element.set_index(len(self._array))

    def get_full(self, indeces):
        return list(x for x in self._array if x.index in indeces)
