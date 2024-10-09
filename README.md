# __Stock Market Simulator__

is a tool designed to provide a realistic environment for testing and backtesting intraday equity trading strategies in stocks in Nifty 500 Index of NSE.


## Author

#### author -   Diya Hansaria

#### edX username - diya_371

#### city, country - New Delhi, India

## Files
__final_list.csv__ - This csv file contains the list of all the stocks of NIFTY 500 and the stock entered by user (whether full name or ticker name) is verified against this list.

__requirements.txt__ - is a list of all the pip installable libraries used in the project and they can be installed together by doing

``` pip install -r requirements.txt ```

**LIBRARIES used in the project**

1: _colorama_ - is used to give a a little splash of green colour when profit is printed and red when loss is printed to add a little fun element

2:- _prettytable_ - is used to print the profit/loss statement at the end to give the user a chance to review their performance

3:- _yfinance_ - is used to gain access to real time data of stocks

4:- _csv_ - is used to work with the csv file of list of stocks of NIFTY 500.

5:- numpy - is used to work with the array of data obtained about the stocks.

6:- threading - for parallel execution so that while user is waiting for their stock to sell, they can execute other functions

7:- queue:- to connect errors in thread to error handling in the main function


## Features

- buy stocks at market price
- buy stocks by setting a custom price
- sell your owned stocks in partial quantities to average
- sell your stocks at market price or by setting a custom price
- get a list of instructions and commands in the middle of program by entering help
- view a profit/loss statement at the end of program to review your performance



## Usage/Examples

```python project.py```

The program starts running.
### Buying a Stock
 The user can buy a stock at any time using

``` new trade ```

They are asked three questions.
```
What to buy? tatasteel
Buy at what price?
How much quantity?
```
1 - Enter the stock's ticker symbol or full name (case insensitive)

2 - Specify a desired purchase price (optional).

If no price is provided, the stock will be bought at the current market price.

3 -
If buy price specified is more than current market price, the stock will automatically be bought at market price.

4- The user can't execute any functions if custom price is specified until the custom price is reached

5 - An positive integral quantity should be specfied. If no quantity or decimal or negative quantity is given, quantity is automatically assumed to be 1.


The user has the ability to obtain the set of commands or instructions used using ```help```

### To sell a stock

Type ```sell.```
Two questions are asked
```
What price to sell it at?
How much quantity?
```

1 - If you want to sell a specific stock, enter its ticker symbol or full name. example -  ``` sell tatasteel ```
The name of stock entered should be held already by user. Trying to sell a stock not owned will result in error .

2 -  If no stock is specified, the earliest purchased stock in your holdings will be sold.

3 - Enter the desired selling price (optional). If no price is provided, the stock will be sold at the current market price.
If the price entered is below the market price, the stock will  be sold at current market price by default.

4 - Enter the quantity to sell (optional). If no quantity is specified, the entire held quantity of the stock will be sold.

5 - Quantity of a stock given to sell should not be greater than quantity of the stock held currently. Quantity should not be negative or decimal point value. In all mentioned cases ```Please enter valid stock quantity``` is displayed

6 - Profit/Loss is displayed each time user sells owned stock in any quantity, example ``` 5 TATASTEEL sold at 153 with 20 (+2 %) ```

7 - After entire quantity of a stock is sold,
``` Please enter valid stock quantity: ValueError ``` message is displayed to alert user

The user has the ability to exit at any time using CTRL + D when a stock is not in waiting to be sold or be bought.

Upon entering CTRL + D to exit program, we get a profit/loss of all trades completed

### Important Notes
1. #### Parallel Execution
 The program allows for simultaneous execution of background tasks (e.g., help, other trades) while awaiting the completion of custom sell orders.

2. #### Prevent Premature Selling

 To avoid "Stock not found" errors, the user should refrain from selling any quantity that is already queued for sale until the original sell order is executed.

## Authors

- [@diya371](https://github.com/diya371)
