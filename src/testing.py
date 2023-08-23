'''
.. py:module: testing

testing, module de test de la docstring.

'''
import typing

def add (a:int, b:int) -> int:
    '''
    .. py:function:: fonction permettant l'addition de deux nombres entiers

    :param a: premier nombre
    :param b: second nombre
    :return: la somme des deux nombres, valeur entières
    :raise TypeError: si l'un des nombres n'est pas un entier

    '''
    if not(isinstance(a, int)) or not(isinstance(b, int)):
        raise TypeError("l'un des nombres n'est pas un entier")
    return a+b

def sous(a:int, b:int)-> int:
    '''
    .. py:function:: fonction permettant de soustraire deux nombres entiers

    :param a: premier nombre
    :param b: second nombre
    :return: la différence du premier et du second nombre
    :raises TypeError: si l'un des nombres n'est pas un entier

    '''
    if not(isinstance(a, int)) or not(isinstance(b, int)):
        raise TypeError("l'un des nombres n'est pas un entier")
    return a - b

class Toto:
    """
    .. py:class: Toto(a)

    :attribute: a

    classe de Test Toto. pour la docstring

    """

    def __init__(self,ab:int):
        self._a = ab

    @property
    def a(self) ->int :
        """
        .. py:method:: a

        accesseur pour obtenir la valeur de l'attribut a

        :return: valeur de l'attribut a

        """
        return self._a

    @a.setter
    def a(self, aaa):
        """
        .. py:method:: a.setter

        accesseur pour modifier l'attribut a

        :param a:
        :return: None
        :raise: TypeError si la valeur fournie n'est pas un entier
        """

        if not(isinstance(aaa,int)):
            raise TypeError("le parametre doit être entier")
        else:
            self._a = aaa

    def __str__(self):
        return (f"Toto [a : {self._a}]")


if __name__ == "__main__" :

    t = Toto(10)
    try:
        res = add(10 ,10)

    except TypeError as e:
        print(f"erreur {e}")
    else :
        print(f"res = {res}")
        print(t)
    finally :
        print ("fin du programme")