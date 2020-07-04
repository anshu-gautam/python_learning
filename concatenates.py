# [a, b, c], [1, 2, 3] → [a, b, c, 1, 2, 3]
array1 = ["a", "b", "c"]
array2 = [1, 2, 3]
for x in array2:
  array1.append(x)
  print(array1)
