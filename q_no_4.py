#n = input("enter a number ")
#n = int(n)
#sum = 0
# while n >= 1:
#sum = sum + n
#n = n-1
# print(sum)

n = 17
# n = int(n)
sum = 0
while n >= 1:
    # print("I am inside while")
    if n % 5 == 0:
      sum = sum + n

    elif n % 3 == 0:
      sum = sum + n
    n-=1
print(sum)
