n = int(input())
div = 2

while(n>1):
  if(n % div == 0):
    n = n / div
    print(int(div))
  else:
    div += 1