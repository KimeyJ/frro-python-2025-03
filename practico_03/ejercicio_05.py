"""Propiedades"""


from turtle import up


class Auto1:
    def __init__(self, nombre, precio):
        self._nombre = nombre.capitalize()
        self._precio = precio

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio(self):
        return round(self._precio, 2)

    @precio.setter
    def precio(self, precio):
        self._precio = precio
    """La clase auto tiene dos propiedades, precio y marca. La marca se define
    obligatoriamente al construir la clase y siempre que se devuelve, se 
    devuelve con la primer letra en mayúscula y no se puede modificar. El precio
    puede modificarse pero cuando se muestra, se redondea a 2 decimales
    
    Restricción: Usar Properties
    
    Referencia: https://docs.python.org/3/library/functions.html#property"""

    # Completar


# NO MODIFICAR - INICIO
auto1 = Auto1("Ford", 12_875.456)

assert auto1.nombre == "Ford"
assert auto1.precio == 12_875.46
auto1.precio = 13_874.349
assert auto1.precio == 13_874.35

try:
    auto1.nombre = "Chevrolet"
    assert False
except AttributeError:
    assert True
# NO MODIFICAR - FIN


###############################################################################


from dataclasses import dataclass

@dataclass
class Auto:
    nombre: str
    _precio: float

    def _init__(self):
        # Convierte la primera letra de "nombre" en mayúscula
        self.nombre = self.nombre.capitalize()

    @property
    def precio(self):
        return round(self._precio, 2)

    @precio.setter
    def precio(self, precio):
        self._precio = precio
    """Re-Escribir utilizando DataClasses"""

    # Completar


# NO MODIFICAR - INICIO
auto = Auto("Ford", 12_875.456)

assert auto.nombre == "Ford"
assert auto.precio == 12_875.46
auto.precio = 13_874.349
assert auto.precio == 13_874.35

try:
    auto.nombre = "Chevrolet"
    assert False
except AttributeError:
    assert True
# NO MODIFICAR - FIN
