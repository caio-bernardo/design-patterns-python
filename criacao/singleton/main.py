from typing import Dict


class Singleton(type):
    _instances: Dict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class AppSettings(metaclass=Singleton):
    def __init__(self):
        self.tema = 'Tema Escuro'
        self.fonte = '10px'


if __name__ == "__main__":
    as1 = AppSettings()
    as1.tema = 'Tema Claro'
    print(as1.tema)

    as2 = AppSettings()
    print(as1.tema)
