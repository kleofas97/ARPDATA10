#  1 opcja - pelna sciazka
# import ARPDATA10_07.ex_02_calculator
#  2 opcja - swoja nazwa
# import ARPDATA10_07.ex_02_calculator as calc        # ZALECANE
# 3 opcja - tylko konkretne funkcje z danego modulu
# from ARPDATA10_07.ex_02_calculator import calculate_sum,calculate_substract  # NIEZALECANE
# 4 opcja pobierz caly modul ( caly plik) pod nazwa
from ARPDATA10_07 import ex_02_calculator             # ZALECANE

def calculate_sum(a, b):
    return a + b

def calculate_substract(a,b):
    return a - b

print('Jetem w module calculator')


if __name__ == "__main__":
    calculator = ex_02_calculator.Calculator(5,6)
    zmienna1 = calculate_sum(1,2)
    zmienna2 = calculate_substract(5,4)
    wynik_dodawania = calculator.get_sum()
    calculator = calculate_sum(1,2)
    # zmianna w nowym branchu
    print('Nowy branch juz dziala!')
    print('Zaczynam maina we Wstepie')