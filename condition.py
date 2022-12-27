days = input("Enter the days")
rate = input("Enter the rate per day")
try:
    total_pay = float(days) * float(rate)
    print(total_pay)

except:
    print("Error, please Enter a numeric input")
