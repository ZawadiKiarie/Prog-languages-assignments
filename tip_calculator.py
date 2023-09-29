# input - total bill amt
#         tip as percentage
#         no of pp splitting bill

total_bill = float(input("Enter the total bill amount: "))
tip_percent = int(input("Enter the tip amount (10, 12, 15): "))
num_of_ppl = int(input("Enter the number of people: "))


bill_for_each = total_bill / num_of_ppl
tip_for_each = (tip_percent/100 * total_bill) / num_of_ppl
payment_for_each = bill_for_each + tip_for_each
rounded_payment_for_each = round(payment_for_each, 2)

print(f"The total amount each person should pay is {rounded_payment_for_each}")