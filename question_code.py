# functions and class inside of a subdirectory called utility and a file called user_input.py
def match_input(prompt, pattern):
    import re
    user_input = input(prompt)
    while not re.match(pattern, user_input, flags=re.IGNORECASE):
        user_input = input(prompt)

    return user_input


def preceded_input(prompt, preced=None):
    if not re.match('^[\n]$', prompt):
        prompt = f'\n{prompt}'
    if prompt[-1] != '\n':
        prompt += '\n'

    print(prompt, end='')

    if preced:
        return input(f'{preced}')
    return input()


def confirmation(data, preced=None, succeed=None):
    """
    data = type that can be converted to a string
    preced, succeed = strings to be displayed respectively around data
    """
    prompt = ''
    if str(data)[0] != '\n':
        prompt += '\n'

    if preced and succeed:
        prompt += f'{preced}{data}{succeed}'
    elif preced:
        prompt += f'{preced}{data}'
    elif succeed:
        prompt += f'{data}{succeed}'
    else:
        prompt += f'{data}'

    if prompt[-1] != '\n':
        prompt += '\n'

    prompt += 'Is this correct?\t[Y/N]'

    user_choice = match_input(prompt, '^[yn]$')

    if re.match('[y]', user_choice, flags=re.IGNORECASE):
        return True
    elif re.match('[n]', user_choice, flags=re.IGNORECASE):
        return False
    else:
        # this should never ever happen, but to be safe
        raise ValueError


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


# class inside of the main project directory in a file called objects.py
class Shift:
    def __init__(self, id):
        from datetime import datetime
        if not isinstance(id, type(datetime.now().date())):
            raise TypeError

        self.id = id

        self.delivery_ids = []
        self.deliveries = []
        self.extra_stop_ids = []
        self.extra_stops = []
        self.carry_out_tips = []
        self.start_time = None
        self.end_time = None
        self.miles_traveled = None
        self.fuel_economy = None
        self.vehicle_compensation = None
        self.device_compensation = None
        self.total_hours = None
        self.extra_tips_claimed = None
        self.split = None

    def input_device_compensation(self):
        from resources.strings import Shift__device_compensation__prompt as\
                prompt
        from utility.user_input import User_Input
        self.device_compensation = User_Input(prompt).money(' device compensation')


# inside a file in the main directory called unit_testing_suite.py
from unittest.mock import patch
import unittest
from objects import Shift

class Test_Shift(unittest.Test_Case):
    def setUp(self):
        from datetime import datetime
        self.shift = Shift(datetime.now().date())

    @patch('objects.Shift.input_device_compensation', return_value=.4)
    def test_input_device_compensation(self, input):
        expected = '$0.4\nIs this correct?\t[Y/N]'
        self.assertEqual(self.shift.input_device_compensation(), expected)
