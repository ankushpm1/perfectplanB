# perfectplanB
#Write a program to prompt the user for days and rate per day to compute total pay. Use 50 days and a rate of 3.5 per day to test the program. Total pay is equal to (days* Rate per day). You should use input to read a string and float() to convert the string to a number.
step1: here we need to take input from user for both days and rate per day
step2: convert those to the float format

days = input("Enter the days")

rate = input("Enter the rate per day")

total_pay = float(days)*float(rate)

print(total_pay)
