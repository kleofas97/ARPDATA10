import unittest
from ARPDATA10_09.ex_01_Rectangle_get_set import Rectangle
import numpy as np

class TestRectangle(unittest.TestCase):

    def setUp(self) -> None:
        self.rect = Rectangle(1, 1)

    def test_setting_text_value_bok1(self):
        new_value = 'tekst'
        expected = self.rect.bok1
        self.rect.bok1 = new_value
        assert expected == self.rect.bok1

    def test_setting_text_value_bok2(self):
        new_value = 'tekst'
        expected = self.rect.bok2
        self.rect.bok1 = new_value
        assert expected == self.rect.bok2

    def test_setting_number_value_bok1(self):
        new_value = 5
        self.rect.bok1 = new_value
        assert 5 == self.rect.bok1

    def test_setting_number_value_bok2(self):
        new_value = 5
        self.rect.bok2 = new_value
        assert 5 == self.rect.bok2

    def test_diagonal_for_square(self):
        rect = Rectangle(4,2)
        result = np.round(rect.get_diagonal(),2)
        assert result == np.round(np.sqrt(20),2)

    def test_area(self):
        rect = Rectangle(4, 5)
        area = rect.get_area()
        assert area == 20



