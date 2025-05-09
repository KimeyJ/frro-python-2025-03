"""Variables y Métodos de Clase"""


class Articulo:
    id = int,
    nombre = ""

    _last_id = 0
    def __init__(self, nombre=""):
        self.id_ = Articulo._last_id + 1
        Articulo._last_id = self.id_
        self.nombre = nombre
    @classmethod
    def _get_last_id(cls):
        return cls._last_id



# NO MODIFICAR - INICIO
art1 = Articulo("manzana")
art2 = Articulo("pera")
art3 = Articulo()
art3.nombre = "tv"

assert art1.nombre == "manzana"
assert art2.nombre == "pera"
assert art3.nombre == "tv"

assert art1.id_ == 1
assert art2.id_ == 2
assert art3.id_ == 3
assert Articulo._last_id == 3
# NO MODIFICAR - FIN
