from currency_converter import *
import time
c = CurrencyConverter()
while True:
    amt = int(input("Amount"))
    x = input("Country1:")
    y = input("Country2:")
    x = c.convert(amt, x, y)
    print(round(x, 2))