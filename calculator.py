def calculate_total(price, quantity, tax=0):
    total = price * quantity
    return total + tax

def apply_discount(total):
    return total * 0.85
