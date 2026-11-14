"""TASK 1 Q.7 - LEAP YEAR CHECK"""

year = int(input("Enter a year: "))

if year % 400 == 0:
    print(year, "is a leap year")
elif year % 100 == 0:
    print(year, "is not a leap year")
elif year % 4 == 0:
    print(year,"is a leap year")
else:
    print(year, "is not a leap year")            
