"""TASK 1 Q.4 FIBONACCI SEQUENCE"""

n = int(input("Enter how many terms: "))

a = 0
b = 1 

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b