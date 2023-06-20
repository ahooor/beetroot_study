print("\n")

products = {
  "Kefir" : {"price" : "12$", "amount": "50"},
  "Milk" : {"price" : "8$", "amount": "120"},
  "Yoghurt" : {"price" : "20$", "amount": "83"}
  }

print(products)

print("\n")

name = input("Product name: ")
price = input("Product price: ")
amount = input("Product amount: ")

print("\n")

if name in products.keys():
    products[name]["price"] = price
    products[name]["amount"] = amount
else:
    products.update({name: {"price": price, "amount": amount}})


print(products)

    # products[name] = price
    # products[name]["price"] = price
    # products[name]["amount"] = amount