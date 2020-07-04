# # for i in range(1, 9):
# #     print(i*"*")

#print this pattern horizontally
# *
# **
# ***
# ****
# *****
# ******
# *******
# ********
max = 9
for x in range (1 , 10):
  print ((max - 1)* " " , x * "*")
  max = max - 1