from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass, field


@dataclass
class Handler(ABC):
    """Classe Abstrata para cada processo de tratamento."""
    sucessor: Handler

    @abstractmethod
    def handle(self, letter: str) -> str: pass


@dataclass
class HandlerABC(Handler):
    sucessor: Handler = field(repr=False)
    LETTERS = ['A', 'B', 'C']

    def handle(self, letter: str) -> str:
        if letter in self.LETTERS:
            return f'{self.__class__.__name__} tratou {letter}.'
        
        return self.sucessor.handle(letter)

@dataclass
class HandlerDEF(Handler):
    sucessor: Handler = field(repr=False)
    LETTERS = ['D', 'E', 'F']

    def handle(self, letter: str) -> str:
        if letter in self.LETTERS:
            return f'{self.__class__.__name__} tratou {letter}.'
        
        return self.sucessor.handle(letter)
        

@dataclass
class HandlerUnsolved(Handler):
    sucessor: Handler = None

    def handle(self, letter: str) -> str:
        return f'Handlers não foram capazes de tratar {letter}.'


if __name__ == "__main__":
    # Definindo a ordem de processamento
    handler_unsolved = HandlerUnsolved()
    handler_def = HandlerDEF(handler_unsolved)
    handler_abc = HandlerABC(handler_def)
    
    # Mandando informações para serem tratadas.
    print(handler_abc.handle('A'))
    print(handler_abc.handle('B'))
    print(handler_abc.handle('C'))
    
    print(handler_abc.handle('D'))
    print(handler_abc.handle('E'))
    print(handler_abc.handle('F'))
    
    print(handler_abc.handle('G'))
    print(handler_abc.handle('H'))
    print(handler_abc.handle('I'))