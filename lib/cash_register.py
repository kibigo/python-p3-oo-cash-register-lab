#!/usr/bin/env python3

class CashRegister:
    
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []

    def add_item (self, title, price, quantity = 1):
        
        for _ in range(quantity):
          self.items.append((title))
          self.total += price 
    
    def apply_discount (self):
        if self.discount > 0:
            discount_amount = (self.discount/100) * self.total
            self.total -= discount_amount
            print (f"After the discount, the total comes to ${self.total:.0f}.")

        elif self.discount <= 0:
            print("There is no discount to apply.")
    
    def void_last_transaction(self):
        all_item = []
        last_item = all_item.append(self.total)

        item_last = last_item.pop()

        self.total -= item_last
