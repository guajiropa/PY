# FILENAME  :   oop_shopping.py
# AUTHOR    :   Robert James Patterson
# DATE      :   4/29/2017
# SYNOPSIS  :   Build an OOP cart that user can enter, add and remove items

# Import the classes used by this program
import sales.shopping_cart, sales.shopping_order

# This is the 'main' funciton
cart = sales.shopping_cart.Cart()
order = sales.shopping_order.Order()
order.get_input()

while not order.quit:
    cart.process(order)
    order = sales.shopping_order.Order()
    order.get_input()
    
print(cart)
