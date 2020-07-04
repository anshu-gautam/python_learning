def maxElement(arr):
    max = arr[0]
    for x in arr:
        if x > max:
            max = x

    return max


def minElement(arr):  # [23, 45, 1, 89, 77]
    min = arr[0]
    for x in arr:
        if x < min:
            min = x
    return min


listx = []
num = int(input("no of numbers in list"))

for n in range(num):
    numbers = int(input("enter a numbers"))
    listx.append(numbers)

print("maximum element in the lis is ",  maxElement(listx),
      "\nminimum element in the list is", minElement(listx))
