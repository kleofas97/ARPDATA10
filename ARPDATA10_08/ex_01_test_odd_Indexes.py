# napisz funkcje ktora njapierw sprawdzi czy input jest stringiem
# a potem zwroci co druga litere, zaczynajac od 2 litery
import unittest
import ARPDATA10_08.ex_01_odd_Indexes as source


class TestOddIndexes(unittest.TestCase):

    def test_odd_indexes_normal_use(self):  # using unittest class
        self.assertEqual(source.odd_indexes('Teleturniej'), 'eeune')

    def test_odd_indexes_normal_use_with_assert(self):
        assert source.odd_indexes('Tekst'), 'es'

    def test_odd_indexes_one_letter(self):
        assert source.odd_indexes('a') == ""

    def test_odd_indexes_empty_text(self):
        self.assertEqual(source.odd_indexes(''), '')

    def test_odd_indexes_wrong_input_number(self):
        self.assertEqual(source.odd_indexes(5), None)

    def test_odd_indexes_wrong_input_list(self):
        self.assertEqual(source.odd_indexes([1,2,3]), None)