from colorama import Fore, Style
from prettytable import PrettyTable
import csv
import yfinance as yf
import numpy as np
import threading
import queue

exception_queue = queue.Queue()

lock = threading.Lock()
running = False
eof_flag = False
object_name_count = []
class Stock:
    object_count = []

    def __init__(self,stock,buy_at,quantity):

        stock = stock.upper()
        self.stock = stock
        self.profit = 0
        ticker = yf.Ticker(self.stock+".NS")
        if buy_at:
            flag = True
            while flag == True:
                array = get_the_price(ticker)
                if array[-1,3] <= float(buy_at):
                    self.buy_at = array[-1,3]
                    flag = False

        else:
            array = get_the_price(ticker)
            self.buy_at = array[-1,3]


        if quantity.isdigit() :
            self.quantity = int(quantity)
            self.end_quantity = quantity

        else:
            self.quantity = 1


    def sell(self,table):

        global running
        try:
            ticker = yf.Ticker(self.stock +".NS")
            price = input("what price to sell it at ")
            how_many = input("How many to sell ")
            if price:
                while True:
                    array = get_the_price(ticker)
                    if array[-1,3] >= float(price):
                        new_price = array[-1,3]
                        break

            else:
                array = get_the_price(ticker)
                new_price = array[-1,3]

            if not(how_many):
                how_many = self.quantity
            elif how_many and int(how_many) > self.quantity:
                raise ValueError("ValueError")
            elif int(how_many) < 0:
                raise ValueError("ValueError")
            else:
                how_many = int(how_many)

            profit = ((new_price) - float(self.buy_at))*how_many
            percent_profit = round(profit*100/float(self.buy_at),2)
            if profit >= 0:
                print(f"{how_many} {self.stock} sold at {new_price} with" + Fore.GREEN + f" +{profit} {percent_profit} %)",end="")
                print(Style.RESET_ALL)

            else:
                print(f"{how_many} {self.stock} sold at {price} with " + Fore.RED + f"{profit} {percent_profit} %)",end="")
                print(Style.RESET_ALL)


            self.profit += profit
            self.quantity = self.quantity - how_many
            if self.quantity == 0:
                table.add_row([self.stock.upper(), self.buy_at, self.end_quantity, self.profit])
                del self
                with lock:
                    running = False
            else:
                with lock:
                    running = False

        except ValueError as e:
            exception_queue.put(e)






    def info(self):
        return f"{self.quantity} {self.stock.upper()} bought at {self.buy_at}"
    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self,stock):
       self._stock = convert(stock)


def get_the_price(ticker):
    price = ticker.history(period="1d", interval="1m")
    array = np.array(price)
    return array
def new_trade():
    global object_name_count
    ticker = (input("What to buy? ")).strip()
    price = input("Buy at what price? ").strip()
    quantity = input("How much quantity? ").strip()
    stock1 = Stock(ticker,price,quantity)
    Stock.object_count.append(stock1)
    object_name_count.append(stock1.stock)
    print(stock1.info())
    return stock1

def convert(x):
    with open("final_list.csv") as file:
        reader = csv.reader(file)
        flag = False
        for row in reader:
            values = row[0].split("_")
            if x.upper().replace(" ", "") == values[0]:
                x = values[0]
                flag = True
            elif x.upper().replace(" ", "") == values[1]:
                x = values[0]
                flag = True
        if not flag:
            raise IndexError
        else:
            return x






def open_page():
    global eof_flag
    global running
    while not(eof_flag):

        table = PrettyTable()
        table.field_names = ["Stock","Buy Price","Quantity","Profit/Loss"]
        for i in range(100):
            try:
                x = input()
                if x.lower().strip() == "help":
                    print('''\t\tInstructions\n1. Type new trade in terminal to buy a stock
                      \n2. Enter full name of stock or ticker name of stock
                      \n3. Enter a buy price lower or equal to current market price
            \n4. If price or quantity field is left empty, current market price
    nd quantity 1 are the default values respectively
                        \n5. To sell a stock Type sell and the stock you want to sell to
                        \n6. Ensure that it is a stock you already have
                        \n7. Enter ctrl+d to exit the program''')
                if "new trade" in x.lower():
                    stock1 = new_trade()
                if "sell" in x.lower() and len(x) > 5:
                    length = len(Stock.object_count)
                    y = convert(x[5:])
                    while length > 0:
                        if y == Stock.object_count[length-1].stock:
                            stock1 = Stock.object_count[length-1]
                            t = threading.Thread(target = stock1.sell, args = (table,))
                            with lock:
                                running = True
                            t.start()
                        length-=1


                elif "sell" in x.lower():
                    stock1 = Stock.object_count[0]
                    t2 = threading.Thread(target = stock1.sell, args = (table,))
                    with lock:
                        running = True
                    t2.start()

                while not exception_queue.empty():
                    exception = exception_queue.get()
                    print(f"Please enter valid stock quantity({exception})")

            except IndexError:
                print("Please enter valid stock name")
            except EOFError:
                print(table)
                print("                    Happy Trading 😊")
                exit()




def main():
    open_page()

if __name__ == "__main__":
    main()
