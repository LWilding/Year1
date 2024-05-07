#!/usr/bin/env python3

if __name__ == '__main__':
    pass

print(f"Beckett Pizza Plaza 4-for-3 Offer")

prices = []
for i in range(4):
    while True:
        try:
            pizza_prices = float(input(f"Enter Price of Pizza #{i+1}: "))
            if 0 < pizza_prices:
                prices.append(pizza_prices)
                break
            else:
                print("Please enter a valid price!")
        except ValueError:
            print("Please enter a valid price!")


total = sum(prices)
free_pizza = min(prices)

print(f"Order Total is £{total - free_pizza}, a fabulous discount of {free_pizza / total * 100:.0f}% ")
