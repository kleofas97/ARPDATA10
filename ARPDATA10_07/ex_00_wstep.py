#  1 opcja - pelna sciazka
# import ARPDATA10_07.ex_02_calculator
#  2 opcja - swoja nazwa
# import ARPDATA10_07.ex_02_calculator as calc        # ZALECANE
# 3 opcja - tylko konkretne funkcje z danego modulu
from ARPDATA10_07.ex_02_calculator import calculate_sum,calculate_substract  # NIEZALECANE
# 4 opcja pobierz caly modul ( caly plik) pod nazwa
from ARPDATA10_07 import ex_02_calculator             # ZALECANE

def calculate_sum(a, b):
    return a + b

def calculate_substract(a,b):
    return a - b

print('Jetem w module calculator')


if __name__ == "__main__":
    print('Zaczynam maina w Kalkulatorze')
    print(calculate_sum(2, 3))





if __name__ == "__main__":
    print('Zaczynam maina we Wstepie')
    print(ex_02_calculator.calculate_sum(2, 3))