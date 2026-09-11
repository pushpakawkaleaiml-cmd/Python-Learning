def apply_discount(price, discount):
    discount_amount = price * (discount / 100)
    final_price = price - discount_amount
    return final_price


price = float(input("Enter the price: "))
discount = float(input("Enter discount percentage: "))

result = apply_discount(price, discount)

print("Final price:", result)