class NumberTranslator:
    '''
        A class for translating a given integer into its verbal equivalent

        Attributes
        ----------
        UNIQUE_NUMBERS -> dict[int:str]
            a dictionary of the integers from 0 to 19 as the keys, and their verbal equivalents as the values

        TENS -> dict[int:str]
            a dictionary of the tens (10, 20, ..., 80, 90) as the keys, and their verbal equivalents as the values

        Methods
        -------
        translate(number)
            translates the given integer into its verbal equivalent
        
        _translate_tens(number)
            translates the given, presumed tens number, into its verbal equivalent
        
        _translate_hundreds(number)
            translates the given, presumed hundreds number, into its verbal equivalent
    '''


    UNIQUE_NUMBERS = {
        0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 
        6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 
        11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 
        16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen'
    }

    TENS = {
        2:'twenty', 3:'thirty', 4:'forty', 5:'fifty', 6:'sixty', 7:'seventy', 8:'eighty', 9:'ninety'
    }


    def translate(self, number: int) -> str:
        '''
            Parameters
            ----------
            number -> int
                an int from 0 to 1000
            
            Returns 
            -------
            str
                the verbal equivalent of the number given
        '''
        # assert for valid range and call function according to buckets (1s, 10s, 100s, or 1000s)
        assert 0 <= number <= 1000

        if 0 <= number <= 19:
            return self.UNIQUE_NUMBERS[number]
        elif 20 <= number <= 99:
            return self._translate_tens(number)
        elif 100 <= number <= 999:
            return self._translate_hundreds(number)
        else:
            return 'one thousand'


    def _translate_tens(self, number: int) -> str:
        '''
            Parameters
            ----------
            number -> int
                an int from 0 to 99

            Returns
            -------
            str
                the verbal equivalent of the given number
        '''
        # check for trickle-down from 100s and switch to 1s if number is not 10s
        if not number // 10:
            return self.UNIQUE_NUMBERS[number%10]
        elif number in self.UNIQUE_NUMBERS:
            return self.UNIQUE_NUMBERS[number]

        # check if postfix digit exists (is > 0) and append to the return string if it does
        postfix = ''
        ones = number % 10
        if ones:
            postfix = '-' + self.UNIQUE_NUMBERS[number%10]

        return self.TENS[number//10] + postfix
    

    def _translate_hundreds(self, number: int) -> str: 
        '''
            Parameters
            ----------
            number -> int
                an int from 100 to 999

            Returns
            -------
            str
                the verbal equivalent of the given number
        '''

        # check if postfix number exists using _translate_tens and append to the return string if it does
        postfix = self._translate_tens(number%100)
        postfix = ' and ' + postfix if postfix != 'zero' else ''

        return self.UNIQUE_NUMBERS[number//100] + ' hundred' + postfix 
        

            


            

