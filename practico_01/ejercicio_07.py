"""Slicing."""

import math as mt

def es_palindromo(palabra: str) -> bool:
    return True if palabra == palabra[::-1] else False
 
   pass # Completar

# NO MODIFICAR - INICIO
assert not es_palindromo("amor")
assert es_palindromo("radar")
assert es_palindromo("")
# NO MODIFICAR - FIN


###############################################################################

def mitad(palabra: str) -> str:
    return palabra[:mt.ceil(len(palabra)/2)]
    pass # Completar



# NO MODIFICAR - INICIO
assert mitad("hello") == "hel"
assert mitad("Moon") == "Mo"
assert mitad("") == ""
# NO MODIFICAR - FIN
