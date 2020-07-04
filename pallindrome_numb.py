def rev(num):
    num_len = len(str(num))
    result = 0
    while num_len > 0:
        result = result * 10 + num % 10
        num = int(num / 10)
        num_len -= 1
    return result

num = int(input('Enter a number: '))
print(rev(num))
