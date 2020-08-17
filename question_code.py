def decimal(prompt, preced=None, places=None):
    """
    preced = type that can be converted into string | comes before user input
    places = integer | represents the number of decimal places
    """
    error_message = '\nERROR: Please enter a whole or decimal number (base 10)'
    if places and not isinstance(places, int):
        raise TypeError('places value must be type integer')

    while True:
        try:
            user_input = float(preceded_input(prompt, preced))
        except ValueError:
            print(error_message)
            continue
        else:
            if places:
                return round(user_input, places)
            else:
                return user_input
                

class User_Input():
    def __init__(self, prompt):
        self.prompt = prompt

    def money(self, succeed=None):
        money = decimal(self.prompt, '$', 2)
        if isinstance(succeed, str):
            while not confirmation(money, '$', succeed):
                money = decimal(self.prompt, '$', 2)
        elif not succeed:
            while not confirmation(money, '$'):
                money = decimal(self.prompt, '$', 2)
        elif succeed:
            raise TypeError('succeed must be able to be converted to string')

        return money


def input_device_compensation(self):
    from resources.strings import Shift__device_compensation__prompt as\
            prompt
    from utility.user_input import User_Input
    self.device_compensation = User_Input(prompt).money(' device compensation')


from unittest.mock import patch
import unittest

@patch('objects.Shift.input_device_compensation', return_value=.4)
def test_input_device_compensation(self, decimal):
    expected = '$0.4\nIs this correct?\t[Y/N]'
    self.assertEqual(self.shift.input_device_compensation(), expected)
