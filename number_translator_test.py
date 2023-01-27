import unittest
import csv
from number_translator import NumberTranslator


class TestTranslator(unittest.TestCase):
    '''
        A class for testing the number translator

        Attributes
        ----------
        _verbal_equivalents_list -> list[list[str]]
            a list of the verbal equivalents of the numbers 0 through 1000

        _conversions -> dict[int:str]
            a dictionary of all the integers from 0 to 1000 as the keys and their verbal equivalents as the values

        _test_translator -> NumberTranslator
            the translator being tested


        Methods
        -------
        test_tens()
            tests the tens numbers (20 to 99, since 0-19 is just a dictionary lookup)

        test_hundreds()
            tests the hundreds numbers (100, 999)

        test_number_translator()
            tests the number translator for all numbers in the required data set
    '''

    # open verbal numbers from csv, filter contents, and map given verbal
    # numbers to ints from 1 to 1000
    with open('verbal_equivalents.csv', 'r') as verbal_equivalents:
        _verbal_equivalents_list = (line[0].replace(
            '\n', '') for line in csv.reader(verbal_equivalents))
        _conversions = dict(zip(range(0, 1001), _verbal_equivalents_list))

    _test_translator = NumberTranslator()

    def test_tens(self):
        for num in range(20, 100):
            self.assertEqual(
                self._test_translator._translate_tens(num),
                self._conversions[num])

    def test_hundreds(self):
        for num in range(100, 1000):
            self.assertEqual(
                self._test_translator._translate_hundreds(num),
                self._conversions[num])

    def test_number_translator(self):
        for num in self._conversions:
            self.assertEqual(
                self._test_translator.translate(num),
                self._conversions[num])


if __name__ == '__main__':
    unittest.main()
