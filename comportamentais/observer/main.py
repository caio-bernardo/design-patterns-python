from abc import ABC, abstractmethod
from typing import Dict, List


class IObserver(ABC):
    @abstractmethod
    def update(self) -> None: pass


class IObservable(ABC):
    """ Observable """

    @property
    @abstractmethod
    def state(self): pass

    @abstractmethod
    def add_observer(self, observer: IObserver) -> None: pass

    @abstractmethod
    def remove_observer(self, observer: IObserver) -> None: pass

    @abstractmethod
    def notify_observers(self) -> None: pass


class WeatherStation(IObservable):
    """ Observable """
    def __init__(self) -> None:
        self._observers: List[IObserver] = []
        self._state: Dict = {}

    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self, state_update: Dict) -> None:
        new_state: Dict = {**self._state, **state_update}
        if new_state != self._state:
            self._state = new_state
            self.notify_observers()

    def add_observer(self, observer: IObserver) -> None:
        self._observers.append(observer)

    def remove_observer(self, observer: IObserver) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_observers(self) -> None: 
        for observer in self._observers:
            observer.update()
    
    def reset_state(self):
        self._state = {}
        self.notify_observers()


class Smartphone(IObserver):
    def __init__(self, name, observable: IObservable) -> None:
        self.name = name
        self.observable = observable
    
    def update(self) -> None:
        observable_name = self.observable.__class__.__name__ 
        print(f'{self.name} o objeto {observable_name} atualizado ->\
         {self.observable.state}')


if __name__ == "__main__":
    weather_station = WeatherStation()
    smartphone = Smartphone('samsung', weather_station)
    other_smartphone = Smartphone('iphone', weather_station)

    weather_station.add_observer(smartphone)
    weather_station.add_observer(other_smartphone)

    weather_station.state = {'temperature': '25'}
    weather_station.state = {'humidity': '67'}
    weather_station.remove_observer(smartphone)
    weather_station.reset_state()