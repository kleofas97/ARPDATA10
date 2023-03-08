# uzywanie @property do zabezpieczenia zmiennych

# artykul z wytlumaczeniem: https://www.geeksforgeeks.org/difference-between-attributes-and-properties-in-python/
class Calculator:

    def __init__(self, a, b):
        self._a = a
        self._b = b

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self,nowa_a):
        print(f'Ustawiam a na {nowa_a}')
        if isinstance(nowa_a,(int,float)):
            self._a = nowa_a
        else:
            # liczba nie jest numerem!
            print(f'Nie zmieniono wartoscli liczba a = {self._a}, poniewaz podano wartosc : {nowa_a}')


    @property
    def b(self):
        print('Getting Value')
        return self._a

    @b.setter
    def b(self, nowe_b):
        print(f'Ustawiam b na {nowe_b}')
        # tu moge napisac np. sprawdzanie czy liczba jest numerem!
        self._b = nowe_b

    def get_sum(self):
        return self._a + self._b

    def get_substract(self):
        return self._a - self._b

    def get_multiply(self):
        return self._a * self._b

    def get_divide(self):
        return self._a / self._b

