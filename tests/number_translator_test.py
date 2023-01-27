import unittest
import csv
from number_translator import NumberTranslator

class TestTranslator(unittest.TestCase):
    with open('verbal_equivalents.csv','r') as verbal_equivalents:
        verbal_equivalents_list = (line[0].replace('\n','') for line in csv.reader(verbal_equivalents))
        ACTUAL_CONVERSIONS = dict(zip(range(1,1001),verbal_equivalents_list))

    def test_number_translator(self):
        translator = NumberTranslator()
        
if __name__ == '__main__':
    unittest.main()