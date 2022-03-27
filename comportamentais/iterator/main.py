from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from collections.abc import Iterator, Iterable
from typing import Any


@dataclass
class MyIterator(ABC, Iterator):
    _collection: list[Any]
    _index = 0

    def __next__(self):
        try: 
            item = self._collection[self._index]
            self._index = self.to_position()
            return item

        except IndexError:
            raise StopIteration

    # Impletado o Padrão Template Method para Iterações customizaveis.
    @abstractmethod
    def to_position(self): pass


@dataclass
class ReversedIterator(MyIterator):
    _index = -1

    def to_position(self):
        return self._index - 1


@dataclass
class MyList(Iterable):
    _my_list: list[Any] = field(default=list)

    def __iter__(self) -> Iterator:
        return MyIterator(self._my_list)
    
    def __str__(self) -> str:
        return f'{self.__class__.__name__}({self._my_list})'

    @property
    def reversed(self):
        return ReversedIterator(self._my_list)

if __name__ == "__main__":
    mylist = MyList([1, 2, 3, 4, 5, 6])

    print(mylist)

    for c in mylist.reversed:
        print(c)
