

def find(listx, number):
  for x in listx :
    if x == number:
      return True
  return False 

listx = [33,66,24,98]
n = int(input ("enter a number: ")) 
print (find(listx, n))    