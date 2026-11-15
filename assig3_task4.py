Prices = [100,250,400,1200,50]
gst = 18
add_gst = list(map(lambda x: x + x*gst/100, Prices ))
print(f"The original price is {Prices}")
print(f"The new price list after gst is {add_gst}")