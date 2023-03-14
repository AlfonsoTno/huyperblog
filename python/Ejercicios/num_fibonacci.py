

def fibonacci(max_number: int):
    """Genera una lista con números fibonacci de acuerdo.

    Args:
        max_number (int): Recibe el valor de la cantidad de números a mostrar.

    Returns:
        lista_fibonacci: lísta con los números fibonacci
    """
    num_anterior, num_actual = 0, 1
    lista_fibonacci = []
    
    if max_number == 1:
        lista_fibonacci = [0]
        print(lista_fibonacci)
    else:
        lista_fibonacci = [0, 1]
        for i in range(0, max_number-2):
            lista_fibonacci.append(num_anterior + num_actual)
            num_anterior, num_actual = num_actual, lista_fibonacci[-1]
                
        print(lista_fibonacci)
    return lista_fibonacci


while True:
    try:
        max_number= int(input('Ingresa un número entero mayor a 0: '))
        if max_number > 0:
            break 
            
        print('Ingresa un número mayor a 0')    

    except ValueError:
        print('Solo puedes ingresar un número entero')

fibonacci(max_number)




