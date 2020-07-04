#for x in range(1, 13):
 #   for y in range(1, 11):
#        print(x, y, x*y)

x = 2020
years = 0
while years != 20:
  while 1:
    if x % 4 == 0:
      print(x)
      years += 1
      x = x + 1
      break
    else:
      x = x + 1
