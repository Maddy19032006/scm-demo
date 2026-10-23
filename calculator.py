
def calculate_total(price, quantity):
    return price * quantity

def get_order_summary(price, quantity):
    total = calculate_total(price, quantity)
    return f"Order total: {total}"
