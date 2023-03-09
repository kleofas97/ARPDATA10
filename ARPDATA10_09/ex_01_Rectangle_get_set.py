# Napisz klase Rectangle
# dodaj atrybuty bok1 bok2 (inicjowane na poczatku, bez sprawdzania czy sa ok)
# dodaj @property dla obu bokow razem ze sprawdzaniem czy parametr jest poprawny (jest liczba)
# metody get area i get przekatna (twierdzenie pitagorasa)
import math

class Rectangle:

    def __init__(self, bok1, bok2):
        self._bok1 = bok1
        self._bok2 = bok2

    @property
    def bok1(self):
        return self._bok1

    @bok1.setter
    def bok1(self, nowa_wartosc):
        if isinstance(nowa_wartosc, (int, float)):
            self._bok1 = nowa_wartosc
        else:
            print('Podana wartosc nie jest liczba')

    @property
    def bok2(self):
        return self._bok2

    @bok2.setter
    def bok2(self, nowa_wartosc):
        if isinstance(nowa_wartosc, (int, float)):
            self._bok2 = nowa_wartosc
        else:
            print('Podana wartosc nie jest liczba')

    def get_area(self):
        return self._bok1 * self._bok2

    def get_diagonal(self):
        return math.sqrt(self._bok1**2 + self._bok2**2)

rect = Rectangle(3,4)
print(rect.get_area())
print(rect.get_diagonal())