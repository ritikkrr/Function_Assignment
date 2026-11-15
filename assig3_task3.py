price = lambda x : x + x*18/100
amount = 100
print(price(amount))
discount = 7
price2 = lambda y: (y + (y*18/100)) - (y*discount/100)
print(price2(amount))