from abc import ABC, abstractmethod


class Abstract(ABC):
    def template_method(self): # criado para não ser sobescrito
        self.hooks()
        self.operation1()
        self.operation2()

    # Note que como o hooks não é abstrato suas classes filhas não são
    #  obrigadas a usar este metodo
    def hooks(self): pass

    @abstractmethod
    def operation1(self): pass

    @abstractmethod
    def operation2(self): pass

class Concrete1(Abstract):
    def operation1(self):
        print('Operação 1')

    def operation2(self):
        print('Operação 2')
    
    def hooks(self):
        print('Usando o hook')

class Concrete2(Abstract):
    def operation1(self):
        print('Operação 1 de maneira diferente')

    def operation2(self):
        print('Operação 2 de maneira diferente')


if __name__ == "__main__":
    c1 = Concrete1()
    c1.template_method()