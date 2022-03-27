from __future__ import annotations
from copy import deepcopy
from dataclasses import dataclass, field


# É preciso que o Memento seja imutavel, __setattr__ faria isso também.
@dataclass(frozen=True)
class Memento:  # The one who remembers
    _save: dict

    @property
    def save(self) -> dict:
        return self._save


# Aqui entra o Command
@dataclass
class CareTaker: # A brigde for the past and the present
    _originator: FileEditor
    _mementos: list[Memento] = field(default_factory=list)

    def backup(self):
        self._mementos.append(self._originator.save_file())
    
    def restore(self):
        if not self._mementos == []:
            self._originator.restore(self._mementos.pop())
        
        return


# Originator
@dataclass
class FileEditor:  # The one who makes history
    file_name: str = 'Unnamed'
    content: str = ''

    def save_file(self) -> Memento:
         return Memento(deepcopy(self.__dict__))

    def restore(self, memento: Memento):
        self.__dict__ = memento.save


if __name__ == "__main__":
    file1 = FileEditor('Titulo1', 'Lorem Ipsum...')
    caretaker = CareTaker(file1)
    
    caretaker.backup()
    print(file1)

    print()

    file1.file_name = 'Novo Titulo'
    print(file1)

    print()

    caretaker.restore()
    print(file1)