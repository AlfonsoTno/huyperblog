"""Este es el Docstring del módulo main""" #Docstring del Módulo
# Docstring
# __doc__


class User:
    """Permite representar un usuario.""" #Docstring de la clase

    def __init__(self, username: str, password: str) -> None:
        #Docstring del método 
        """Permite instanciar un objeto de tipo User. 
        
        Args:
            usernmae (str): El username del usuario.
            password (str): El password del usuario.
        """

        self.username = username
        self.password = password



def palindromo(sentence: str) -> bool:
    #Docstring de la funcion
    """Permite conocer su un string es, o no, un palindromo.

     Args:
        sentence (str): String a evaluar.

    Returns:
        bool: True o False

    Examples: 
    """
  
    sentence = sentence.lower().replace(' ', '')
    return sentence == sentence[::-1]