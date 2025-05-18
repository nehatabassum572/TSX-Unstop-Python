# 3. Write a script that checks if a given year is a leap year 
# (divisible by 4, but not by 100 unless also divisible by 400).
year = int(input("Enter a year: "))
if (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0)):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")