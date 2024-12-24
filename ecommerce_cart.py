def calculate_total_price(cart_items):
    if not cart_items:
        return "The cart is empty."
    
    total_price = sum(cart_items.values())
    
    if len(cart_items) > 5:
        discount = total_price * 0.10
        total_price -= discount
    
    return total_price

cart_items = {
    'Laptop': 50000,
    'Headphones': 2000,
    'Mouse': 500,
    'Keyboard': 1500,
    
}

total = calculate_total_price(cart_items)

if isinstance(total, str):  
    print(total)
else:
    print(f"Total Price: {total}")

