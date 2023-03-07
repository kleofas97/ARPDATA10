# zadanie
# napisz klase Calculator
# 2 atrybuty ( okreslane przy inicjacji) a i b
# 4 metody do obliczen - (ktore zwracaja wynik odpowiednio mnozenia, dzielenia, dodawania i odejmowania)

# upgrade - 1 - dodaj liczenie ile operacji juz bylo
#     - w danym kalkulatorze
# - we wszystkich kalkulatorach


# upgrade - 2 - bezpieczna zmiana danych w klasach
# https://www.geeksforgeeks.org/difference-between-attributes-and-properties-in-python/
# gettery i settery <-- dekorator property

class Calculator:
    number_of_all_operation = 0

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.total_number_of_operation = 0

    def get_sum(self):
        self.total_number_of_operation += 1
        Calculator.number_of_all_operation +=1
        return self.a + self.b

    def get_substract(self):
        self.total_number_of_operation += 1
        Calculator.number_of_all_operation += 1
        return self.a - self.b

    def get_multiply(self):
        self.total_number_of_operation += 1
        Calculator.number_of_all_operation += 1
        return self.a * self.b

    def get_divide(self):
        self.total_number_of_operation += 1
        Calculator.number_of_all_operation += 1
        return self.a / self.b

    def get_number_of_operation(self):
        return self.total_number_of_operation
