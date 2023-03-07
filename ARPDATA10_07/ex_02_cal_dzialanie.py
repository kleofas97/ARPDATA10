import ARPDATA10_07.ex_02_calculator as calc
import sys


def main():
    # Zeby pobrac dane od uzytkownika
    # kwargs = dict(arg.split('=') for arg in sys.argv[1:])
    # a = int(kwargs['a'])
    # b = int(kwargs['b'])
    calculator = calc.Calculator(5, 6)
    print(calculator.get_sum())
    print(calculator.get_substract())
    print(calculator.get_number_of_operation())  # wypisz 2
    calculator_2 = calc.Calculator(51, 6)
    print(calculator_2.get_sum())
    print(calculator_2.get_substract())
    print(calc.Calculator.number_of_all_operation)  # wypisz 4


if __name__ == "__main__":
    main()
