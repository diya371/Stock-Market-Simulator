import project
import pytest
from unittest.mock import patch
import yfinance as yf

def test():
    assert project.convert("VIP INDUSTRIES") == "VIPIND"
    assert project.convert("Piramal Pharma") == "PPLPHARMA"

class Test_func:
    @patch('builtins.input', return_value='help')
    def open_page(self):
        result = project.open_page()
        self.assertEqual(result, '''\t\tInstructions\n1. Type new trade in terminal to buy a stock
                      \n2. Enter full name of stock or ticker name of stock
                      \n3. Enter a buy price lower or equal to current market price
        \n4. If price or quantity field is left empty, current market price
and quantity 1 are the default values respectively
                     \n5. To sell a stock Type sell and the stock you want to sell to
                      \n6. Ensure that it is a stock you already have
                      \n7. Enter ctrl+d to exit the program''')

 
