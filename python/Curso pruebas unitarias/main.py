# Docstring
# __doc__

def palindromo(sentence: str) -> bool:
    """Permite conocer su un string es, o no, un palindromo.

     Args:
        sentence (str): String a evaluar.

    Returns:
        bool: True o False
    """
  
    sentence = sentence.lower().replace(' ', '')
    return sentence == sentence[::-1]