def adder(n):
    sum = 0
    while n >= 1:
        sum = sum + n
        n = n - 1
    return sum


def multiplier(n):
    product = 1
    while n >= 1:
        product = product * n
        n = n - 1
    return product


n = int(input("enter a number: "))
op = input("enter the operator : ")

if op == "+":
    print("Sum of the numbers are ", adder(n))

elif op == "*":
    print("product of the numbers are ", multiplier(n))
