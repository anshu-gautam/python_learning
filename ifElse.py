# # take a number from users,
# # print OKAY if the remainder of the number divided by 7 is 1
# # print GOOD if the remainder of the number divided by 7 is 2
# # print EXCELLENT if the remainder of the number divided by 7 is anything but not 1 and 2
# x = input("Enter a number")
# x = int(x)

# if x % 7 == 1:
#     print("OKAY")

# elif x % 7 == 2:
#     print("GOOD")

# else:
#     print("EXCELLENT")

# 1. traverse through this list [23, 46, 88, 80, 56] and print "EVEN" if the number is even else print "ODD"
# 2. take a number from user, go till 0 and print the numbers that are divided by 4.

#listx = [23, 46, 88, 80, 56]
#for x in listx:
 #      print (x, " is EVEN")
  #  else:
   #     print (x, " is ODD")
     
     
x = input("enter a number")
x = int(x)
while(x >= 0):
    if x % 4 == 0:
        print (x)
    x = x-1
