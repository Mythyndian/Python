import collections.abc
import copy
from bisect import bisect_right


def _identity():
    return lambda x: x


class SortedList(collections.abc.Sequence):
    @property
    def key(self):
        return self._key

    def __init__(self, sequence=None, key=None):
        self._key = key or _identity()
        # breaks if key is not callable
        assert isinstance(self._key, collections.abc.Callable)
        self._sequence = list(sequence)
        self._sequence.sort(key=key)
        self._sequence.sort()

    def __str__(self):
        return f'SortedList({self._sequence})'

    def __getitem__(self, item):
        return self._sequence[item]

    def __len__(self):
        return len(self._sequence)

    def __delitem__(self, x):
        del self._sequence[x]
        return

    def __setitem__(self, key, value):
        self._sequence[key] = value

    def __iter__(self):
        return iter(self._sequence)

    def __reversed__(self):
        return self._sequence.reverse()

    def __contains__(self, item):
        if item in self._sequence:
            return True
        else:
            return False

    def __copy__(self):
        return copy.copy(self)

    def _find_index(self, value):
        i = bisect_right(self._sequence, value)
        if i:
            return i - 1
        else:
            return 0

    def add(self, value):
        self._sequence.insert(self._find_index(value), value)

    def pop(self, index):
        self._sequence.pop(index)

    def clear(self):
        del self._sequence
        self._sequence = []

    def remove(self, value):
        self._sequence.pop(self._find_index(value))

    def remove_every(self, value):
        while value in self._sequence:
            self._sequence.pop(self._find_index(value))

    def index(self, value):
        return self._find_index(value)

    def count(self, value):
        return self._sequence.count(value)

    def copy(self):
        self.__copy__()

    def extend(self, iterable_object):
        for i in iterable_object:
            self._sequence.append(i)
