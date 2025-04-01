"""Expresiones Booleanas."""


def es_vocal_if(letra: str) -> bool:
    """
    Restricción: Utilizar un if para cada posibilidad con la función lower().
    Referencia: https://docs.python.org/3/library/stdtypes.html#string-methods
    """
    letra = letra.lower()
    if letra == "a": return True
    elif letra == "e": return True
    elif letra == "i": return True
    elif letra == "o": return True
    elif letra == "u": return True
    else: return False
    pass # Completar


# NO MODIFICAR - INICIO
assert es_vocal_if("a")
assert not es_vocal_if("b")
assert es_vocal_if("A")
# NO MODIFICAR - FIN


###############################################################################


def es_vocal_if_in(letra: str) -> bool:
    letra = letra.lower()
    if (letra in ["a","e","i","o","u"]): return True
    else: return False
    pass # Completar


# NO MODIFICAR - INICIO
assert es_vocal_if_in("a")
assert not es_vocal_if_in("b")
assert es_vocal_if_in("A")
# NO MODIFICAR - FIN


###############################################################################


def es_vocal_in(letra: str) -> bool:
    letra = letra.lower()
    return letra in ["a","e","i","o","u"]
    pass # Completar


# NO MODIFICAR - INICIO
assert es_vocal_in("a")
assert not es_vocal_in("b")
assert es_vocal_in("A")
# NO MODIFICAR - FIN
