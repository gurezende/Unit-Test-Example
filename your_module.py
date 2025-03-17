def calculate_discount(total_amount, customer_type):
    if total_amount < 0:
        raise ValueError("Total amount cannot be negative")
    if customer_type not in ["VIP", "Regular"]:
        raise ValueError("Unknown customer type")

    if customer_type == "VIP":
        return total_amount * 0.9  # 10% off
    elif total_amount > 500:
        return total_amount * 0.8  # 20% off
    else:
        return total_amount  # no discount