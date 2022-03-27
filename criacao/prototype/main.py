from copy import deepcopy
from typing import List


class StringReprMixin:
    def __str__(self) -> str:
        params = ', '.join( [f'{k}={v}' for k, v in self.__dict__.items()])
        return f'{self.__class__.__name__}({params})'
    
    def __repr__(self) -> str:
        return self.__str__()

class Address(StringReprMixin):
    def __init__(self, street: str, number: str) -> None:
        self.street = street
        self.number = number


class Person(StringReprMixin):
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.address: List[Address] = []

    def add_address(self, adress: Address) -> None:
        self.address.append(adress)

    def clone(self):
        return deepcopy(self)

if __name__ == "__main__":
    caio = Person('Caio', 'Bernardo')
    endereco = Address('Moura Ribeiro', '125')
    caio.add_address(endereco)

    maria = caio.clone()
    maria.firstname = 'Maria'

    print(maria)
    print(caio)    
