from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum, auto


class Size(Enum):
    SMALL = auto()
    NORMAL = auto()
    GIANT = auto()


class Ingredients(Enum):
    CHEESE = auto()
    PEPPERONI = auto()
    TOMATE = auto()
    PINEAPLLE = auto()
    TUNA = auto()
    CHOCOLATE = auto()
    OIGNION = auto()
    CHICKEN = auto()
    MANJERICAO = auto()
    CANDY = auto()


class BorderTypes(Enum):
    THIN = auto()
    NORMAL = auto()
    THICK = auto()


class PizzaBuilder:
    def __init__(self) -> None:
        self.reset()
    
    def reset(self):
        self._pizza = Pizza()

    @property
    def finished_pizza(self):
        pizza = self._pizza
        self.reset()
        return pizza
    
    # Return self permite o encadeamento de metedos
    def pizza_size(self, size: Size):
        self._pizza.size = size
        return self
    
    def pizza_filling(self, filling=Ingredients):
        self._pizza.filling = filling
        return self
    
    def pizza_border(self, border=BorderTypes):
        self._pizza.border = border
        return self
    

@dataclass(repr=False)
class Pizza:
    size: Size = None
    filling: set[Ingredients] = field(default_factory=set)
    border: BorderTypes = None

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.size.name}, ({", ".join([c.name for c in self.filling])}), {self.border.name})'


class PizzaDirector:
    def __init__(self, builder: PizzaBuilder):
        self._builder = builder

    def margerita(self):
        self._builder.pizza_size(Size.NORMAL)
        ingredients = {Ingredients.CHEESE, Ingredients.TOMATE, Ingredients.MANJERICAO}
        self._builder.pizza_filling(ingredients)
        self._builder.pizza_border(BorderTypes.NORMAL)
        return self._builder.finished_pizza
    
    def small_chocolate(self):
        ingredients = {Ingredients.CHOCOLATE, Ingredients.CANDY}
        # Chaining methods
        self._builder.pizza_size(Size.SMALL)\
        .pizza_filling(ingredients)\
        .pizza_border(BorderTypes.THIN)
        return self._builder.finished_pizza
    
    def mega_jumbo(self):
        self._builder.pizza_size(Size.GIANT)
        ingredients = {
            Ingredients.CHEESE, Ingredients.PEPPERONI, Ingredients.OIGNION,
            Ingredients.TOMATE, Ingredients.MANJERICAO, Ingredients.CHICKEN
            }
        self._builder.pizza_filling(ingredients)
        self._builder.pizza_border(BorderTypes.THICK)
        return self._builder.finished_pizza


if __name__ == "__main__":
    director = PizzaDirector(PizzaBuilder())
    pizza1 = director.margerita()
    print(pizza1)

    pizza2 = director.mega_jumbo()
    print(pizza2)

    pizza3 = director.small_chocolate()
    print(pizza3)