"""Type, Comprensión de Listas, Sorted y Filter."""

from typing import List, Union




def numeros_al_final_basico(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    aux = []
    for val in lista:
        if type(val) == type("a"): aux.append(val)
    for val in lista:
        if type(val)==type(1) or type(val)==type(1.0): aux.append(val)
    return aux
    pass # Completar


# NO MODIFICAR - INICIO
assert numeros_al_final_basico([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_comprension(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    aux = [val for val in lista if type(val)==type("a")]
    aux2 = [val for val in lista if type(val)==type(1) or type(val)==type(1.0)]
    return aux+aux2
    pass # Completar

# NO MODIFICAR - INICIO
assert numeros_al_final_comprension([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################
def cmp(x):
    return type(x)==type(1) or type(x)==type(1.0)
    pass

def numeros_al_final_sorted(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    lista.sort(key=cmp)
    return lista
    """Re-escribir utilizando la función sorted con una custom key.
    Referencia: https://docs.python.org/3/library/functions.html#sorted
    """
    pass # Completar


# NO MODIFICAR - INICIO
assert numeros_al_final_sorted([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_filter(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """CHALLENGE OPCIONAL - Re-escribir utilizando la función filter.
    Referencia: https://docs.python.org/3/library/functions.html#filter
    """
    a = filter(lambda x: type(x)==type("a"),lista)
    b = filter(lambda x: type(x)==type(1) or type(x)==type(1.0),lista)
    auxA = list(a)
    auxB = list(b)
    return auxA+auxB
    pass # Completar


# NO MODIFICAR - INICIO
if __name__ == "__main__":
    assert numeros_al_final_filter([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_recursivo(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """CHALLENGE OPCIONAL - Re-escribir de forma recursiva."""
    if not lista: return []
    a = lista[-1]
    b = numeros_al_final_recursivo(lista[:-1])
    if type(a)==type("a"):
        i = 0
        while (i < len(b) and type(b[i])==type("a")): i += 1
        b.insert(i,a)
        return b
    else: 
        b.append(a)
        return b
    pass # Completar

# NO MODIFICAR - INICIO
if __name__ == "__main__":
    assert numeros_al_final_recursivo([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN
