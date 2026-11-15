def process_prices(Prices):
    
    discount_rate = 10
    discounted_price = list(map(lambda x : x - x*discount_rate/100 , Prices))
    filtereded_price = list(filter(lambda y : y > 300, discounted_price))
    return discounted_price, filtereded_price
Prices = [100,500,900,50,750]
discounted_price, filtereded_price = process_prices(Prices)
print(f" These are discounted price {discounted_price} ")
print(f"These are filtered price whose are greater than 300 {filtereded_price}")
 
