Prices = [100,250,400,1200,50,2000,850]
Big = list(filter(lambda x : x > 500, Prices))
Small = list(filter(lambda y : y <= 500, Prices))
print(f"These list are greater than 500 {Big}")
print(f"These list are equal to or less than 500 {Small}")