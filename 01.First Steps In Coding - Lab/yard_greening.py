real_gross = float(input())

normal_price = real_gross * 7.61
discount = normal_price * 0.18
final_price = normal_price - discount

print(f"The final price is: {final_price} lv.")
print(f"The discount is: {discount} lv.")
