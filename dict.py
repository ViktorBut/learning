stock = [
    {"name" : "iPhone Xs Plus", 'stock' : 24, 'price' : 65432.1, 'recommended': ['Samsung Galaxy S10', 'iPhone Xs']},
    {"name" : "Samsung Galaxy S10", 'stock' : 8, 'price' : 50000.0, 'discount': 5000},
    {"name" : "Xiaomi Mi8", 'stock' : 42, 'price' : 38500.5, 'discount': 5000},
   ]
print(stock[0])
stock[0]['price'] -= 10000.1
print(stock[0])