n = int(input("enter size of series"))
a = 0
b = 1
sum = 0
count = 1
print("fibance series ")
while (count <= n):
    a = b
    b = sum
    sum = a+b
    print(sum)
    count += 1
