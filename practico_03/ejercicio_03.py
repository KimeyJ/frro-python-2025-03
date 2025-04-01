"""Dataclasses"""


class Persona:
    def __init__(self,nombre:str,edad:int,sexo:str,peso:float,altura:float) -> None:
        self.nombre: str = nombre
        self.edad: int = edad
        self.sexo: str = sexo
        self.peso: float = peso
        self.altura: float = altura
    
    def es_mayor_edad(self) -> bool:
        return self.edad >= 18

    # Completar


# NO MODIFICAR - INICIO
assert Persona("Juan", 18, "H", 85, 175.9).es_mayor_edad()
assert not Persona("Julia", 16, "M", 65, 162.4).es_mayor_edad()
# NO MODIFICAR - FIN


###############################################################################


from dataclasses import dataclass

@dataclass
class Persona:
    nombre: str
    edad: int
    sexo: str
    peso: float
    altura: float

    def es_mayor_edad(self) -> bool:
        return self.edad >= 18

# NO MODIFICAR - INICIO
assert Persona("Juan", 18, "H", 85, 175.9).es_mayor_edad()
assert not Persona("Julia", 16, "M", 65, 162.4).es_mayor_edad()
# NO MODIFICAR - FIN
