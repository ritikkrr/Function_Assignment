def apply_discount(price,discount_percentage=5): # i want if i miss the discount_percentage value the it's automatically take discount_percentage = 5
    if discount_percentage >60: # i want no one get discount more than 60
        discount_percentage = 60
    discount_value = price - price*discount_percentage/100
    print(f"The amount is {price} and amount after discount is {discount_value}")

apply_discount(1000,10)
apply_discount(500)