import unittest
from ARPDATA10_09.ex_03_String_Merging import merge_strings_Maurycy as merge_strings


class TestStringMerging(unittest.TestCase):
    def test_same_length(self):
        result = merge_strings("pies", "buda")
        expected = "pbiuedsa"
        assert result == expected

    def test_first_text_longer(self):
        result = merge_strings("supermarket", "stop")
        expected = "ssutpoeprmarket"
        assert result == expected

    def test_second_text_longer(self):
        result = merge_strings("stop", "supermarket")
        expected = "sstuoppermarket"
        assert result == expected
