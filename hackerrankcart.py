cartlist = []

class Item:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    
class ShoppingCart:
    def add(obj):
        cartlist.append(obj)

    def total():
        total = 0
        for i in cartlist:
            total = total + i.price
        return total
    
    def len():
        return len(cartlist)


cart1 = Item("salmon",300)
cart2 = Item("coconut",100)
cart3 = Item("shell",50)
cart4 = Item("gas",1200)
cart5 = Item("gold",200)
cart6 = Item("gas",1200)

ShoppingCart.add(cart1)
ShoppingCart.add(cart2)
ShoppingCart.add(cart3)
ShoppingCart.add(cart4)
ShoppingCart.add(cart5)
ShoppingCart.add(cart6)

print(ShoppingCart.len())
print("------------------------")
print(ShoppingCart.total())
print("------------------------")





