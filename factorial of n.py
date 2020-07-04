# factorial of n
n = int(input("enter a number"))
product = 1
while n >= 1:
    product = product * n
    n = n - 1

print(product)
