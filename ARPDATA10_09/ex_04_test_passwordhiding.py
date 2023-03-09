import unittest
from ARPDATA10_09 import ex_04_PasswordHiding



class TestHidePassword(unittest.TestCase):

    def test_normal_tekst(self):
        tekst= "moje_super_tajne_haslo123"
        result = ex_04_PasswordHiding.hide_password(tekst)
        expected = "mo*e_*up*r_*aj*e_*as*o1*3"
        assert result == expected

    def test_short_tekst(self):
        tekst = 'adam'
        result = ex_04_PasswordHiding.hide_password(tekst)
        expected = 'ad*m'
        assert result == expected

    def test_very_short(self):
        tekst = 'ad'
        result = ex_04_PasswordHiding.hide_password(tekst)
        expected = 'ad'
        assert result == expected

    def test_empty_string(self):
        tekst = ''
        result = ex_04_PasswordHiding.hide_password(tekst)
        expected = ''
        assert result == expected
