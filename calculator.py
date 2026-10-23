
def calculate_total(price, quantity):
    return price * quantity * 0.90

def get_order_summary(price, quantity):
    total = calculate_total(price, quantity)
    return f"Discounted order total: {total}"
