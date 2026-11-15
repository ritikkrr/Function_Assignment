
def add_price(prices_list,price):
    #Adds prices to the list.
    prices_list.append(price)

def get_average_price(prices_list):
    # Return average price.
    total = 0
    for i in prices_list:
        total = total + i
    return total/ len(prices_list)
def get_max_price(prices_list):
    # Return the maximum number
    for i in prices_list:
        maximum = max(prices_list)
        return maximum


prices = []
while True:
    print("1 -> Add price")
    print("2-> Show average price")
    print("3-> Show highest price")
    print("q -> Quit")

    choice = input("Enter choice")

    if choice == '1':
        price = float(input("enter price"))
        add_price(prices, price)
    elif choice == '2':
        if len(prices) == 0:
            print("list is empty")
        else :
            avg = get_average_price(prices)
            print(avg)
    elif choice == '3':
        if len(prices) == 0:
            print("list is empty")
        else:
            max_P = get_max_price(prices)
            print(max_P)

    elif choice == 'q':
        break
    else:
        print("Invalid choice")