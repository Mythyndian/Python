import collections.abc

import doctest

_identity = lambda x: x


class SortedList(collections.abc.Sequence):
    @property
    def key(self):
        return self._key

    def __init__(self, sequence=None, key=None):
        self._key = key or _identity
        # breaks if key is not callable
        assert isinstance(self._key, collections.abc.Callable)
        self._sequence = list(sequence)
        self._sequence.sort(key=key)

    def __str__(self):
        return f'SortedList({self._sequence})'

    def __getitem__(self, item):
        pass

    def __len__(self):
        return len(self._sequence)


def main():
    numbers = SortedList([2, 3, 5, 6, 76])
    print(numbers)


if __name__ == '__main__':
    main()
