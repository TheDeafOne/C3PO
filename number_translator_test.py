import unittest
import csv
from number_translator import NumberTranslator

class TestTranslator(unittest.TestCase):
    '''
        A class for testing the number translator

        Attributes
        ----------
        _verbal_equivalents_list -> list[list[str]]
            a list of the verbal equivalents of the numbers 1 through 1000
        
        _conversions -> dict[int:str]
            a dictionary of all the integers from 1 to 1000 as the keys and their verbal equivalents as the values

        _test_translator -> NumberTranslator
            the translator being tested 
    '''


    # open verbal numbers from csv, filter contents, and map given verbal numbers to ints from 1 to 1000
    with open('verbal_equivalents.csv','r') as verbal_equivalents:
        _verbal_equivalents_list = (line[0].replace('\n','') for line in csv.reader(verbal_equivalents))
        _conversions = dict(zip(range(1,1001),_verbal_equivalents_list))
        _test_translator = NumberTranslator()
        

        
if __name__ == '__main__':
    unittest.main()