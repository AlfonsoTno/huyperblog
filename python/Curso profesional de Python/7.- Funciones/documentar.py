# Docstring
# __doc__ (Módulos, Clases, Métodos y Funciones)
# se ejecuta prueba con: python -m doctest documentar.py
def suma(numero_1, numero_2):
    """
    La función suma 2 números enteros.

    Argumentos:
    numero_1 (int)
    numero_2 (int)

    Se retorna la suma de los parámetros.

    >>> suma(10, 20)
    30

    >>> suma(100, 200)
    300

    """
    return numero_1 + numero_2

#print(suma.__doc__)

#print(help(suma))

def resta(numero_1, numero_2):
    """
    >>> resta(100, 200)
    -100
    """
    return numero_1 - numero_2 