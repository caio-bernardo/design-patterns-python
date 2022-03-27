from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    @abstractmethod
    def calculate(self, value: float) -> float: pass


class TwentyPercent(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value - (value * 0.2)


class FifthyPercent(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value - (value * 0.5)


class CustomDiscount(DiscountStrategy):
    def __init__(self, discount: float):
        self.discount = discount / 100        

    def calculate(self, value: float) -> float:
        return value - (value * self.discount)


class NoDiscount(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value


class Order: # Context
    def __init__(self, total: float, discount: DiscountStrategy) -> None:
        self._total = total
        self._discount = discount  # strategy instance
    
    @property
    def total(self):
        return self._total
    
    @property
    def total_wth_discount(self):
        return self._discount.calculate(self.total)
    
if __name__ == "__main__":
    twenty_percent = TwentyPercent()
    order = Order(1000, twenty_percent)
    print(order.total, order.total_wth_discount)
