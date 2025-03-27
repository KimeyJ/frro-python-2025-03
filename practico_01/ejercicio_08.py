"""Any y Sets."""

from typing import Any, Iterable


def superposicion_basico(lista_1: Iterable[Any], lista_2: Iterable[Any]) -> bool:
    for elemento_1 in lista_1:
        for elemento_2 in lista_2:
            if elemento_1 == elemento_2:
                return True      
    return False


# NO MODIFICAR - INICIO
test_list = [1, "hello", 35.20]
assert superposicion_basico(test_list, (2, "world", 35.20))
assert not superposicion_basico(test_list, (2, "world", 30.85))
# NO MODIFICAR - FIN


###############################################################################


def superposicion_in(lista_1: Iterable[Any], lista_2: Iterable[Any]) -> bool:
    for elemento_2 in lista_2:
        if elemento_2 in lista_1:
            return True
    return False



# NO MODIFICAR - INICIO
test_list = [1, "hello", 35.20]
assert superposicion_in(test_list, (2, "world", 35.20))
assert not superposicion_in(test_list, (2, "world", 30.85))
# NO MODIFICAR - FIN


###############################################################################


def superposicion_any(lista_1: Iterable[Any], lista_2: Iterable[Any]) -> bool:
    if any(elemento_2 in lista_1 for elemento_2 in lista_2):
        return True
    return False
    


# NO MODIFICAR - INICIO
test_list = [1, "hello", 35.20]
assert superposicion_any(test_list, (2, "world", 35.20))
assert not superposicion_any(test_list, (2, "world", 30.85))
# NO MODIFICAR - FIN


###############################################################################


def superposicion_set(lista_1: Iterable[Any], lista_2: Iterable[Any]) -> bool:
    l1= set(lista_1)
    l2= set(lista_2)
    if l1.intersection(l2):
        return True
    return False


# NO MODIFICAR - INICIO
test_list = [1, "hello", 35.20]
assert superposicion_set(test_list, (2, "world", 35.20))
assert not superposicion_set(test_list, (2, "world", 30.85))
# NO MODIFICAR - FIN