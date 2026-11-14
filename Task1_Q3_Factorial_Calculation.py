"""TASK 1 Q.3 FACTORIAL CALCULATION"""

num = int(input("Enter a number:- "))

fact = 1

for i in range(1, num + 1):
    fact = fact * i

print("Factorial =", fact)