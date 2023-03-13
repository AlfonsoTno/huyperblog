# assert

""" ejemplo 1 usar Try para mandar errores por mensaje

if __name__ == '__main__':

    try:
        assert 5 == 10, 'Lo sentimos 5 no es igual a 10'
        print('El programa continua con su ejecución')
    
    except AssertionError as error:
        print(error)
"""

def suma_numeros_prositicvos(n1: int, n2: int) -> int:
    """Perminte sumar 2 números enteor positivos.

    Args:
        n2 (int): 
        n1 (int): 

    Returns:
        int
    """
    assert n1 > 0 and n2 > 0, 'Lo sentimos, solo es posible sumar números enteros' 

    return n1 + n2

if __name__ == '__main__':
    resultado =  suma_numeros_prositicvos(-10,20)
    print(resultado)



