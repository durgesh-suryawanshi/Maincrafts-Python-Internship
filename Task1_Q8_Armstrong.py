"""TASK 1 Q.8 - ARMSTRONG NUMBER"""

num = int(input("Enter a number: "))

order = len(str(num))

sum_val = sum(int(digit) ** order for digit in str(num))

if num == sum_val:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
