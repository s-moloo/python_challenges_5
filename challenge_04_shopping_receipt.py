item1_name = input("Enter name for item 1: ")
price1 = float(input("Enter price for item 1: "))

item2_name = input("Enter name for item 2: ")
price2 = float(input("Enter price for item 2: "))

item3_name = input("Enter name for item 3: ")
price3 = float(input("Enter price for item 3: "))

total = float(price1 + price2 + price3)

print(f"-----------------------")
print(f"  {item1_name}   ${price1:.2f}")
print(f"  {item2_name}    ${price2:.2f}")
print(f"  {item3_name}     ${price3:.2f}")
print(f"-----------------------")
print(f"  Total    ${total:.2f}")