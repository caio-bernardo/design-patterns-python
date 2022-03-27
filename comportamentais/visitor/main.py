from __future__ import annotations
from abc import ABC, abstractmethod


class Visitor(ABC):
    @abstractmethod
    def visit_component_a(self, element: ComponentA): 
        pass
    
    @abstractmethod
    def visit_component_b(self, element: ComponentB):
        pass


class ConcreteVisitor1(Visitor):
    def visit_component_a(self, element: ComponentA): 
        print(element.component_a_method(), 'Visitor1')

    def visit_component_b(self, element: ComponentB):
        print(element.component_b_method(), 'Visitor1')


class ConcreteVisitor2(Visitor):
    def visit_component_a(self, element: ComponentA): 
        print(element.component_a_method(), 'Visitor2')

    def visit_component_b(self, element: ComponentB):
        print(element.component_b_method(), 'Visitor2')


class Component(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor):
        pass


class ComponentA(Component):
    def accept(self, visitor: Visitor):
        visitor.visit_component_a(self)
    
    def component_a_method(self):
        return 'A'


class ComponentB(Component):
    def accept(self, visitor: Visitor):
        visitor.visit_component_b(self)
    
    def component_b_method(self):
        return 'B'


def client_code(components: list[Component], visitor: Visitor):
    for component in components:
        component.accept(visitor)

if __name__ == "__main__":
    components = (ComponentA(), ComponentB())

    visitor1 = ConcreteVisitor1()

    client_code(components, visitor1)

    visitor2 = ConcreteVisitor2()

    client_code(components, visitor2)
