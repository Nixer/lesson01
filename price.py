def format_price(price):
    try:
        price = int(float(price))
        return f"Цена: {price} руб."
    except (ValueError, TypeError):
        return "Введено неправильное значение!"


display_price = format_price("56.24")
print(display_price)
