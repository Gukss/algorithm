import math

t = int(input())
list = []

for i in range(t):
  h, w, n = map(int, input().split())
  y = int(n % h)
  x = math.ceil(n / h)
  if x < 10:
    x = '0' + str(x)
  else:
    x = str(x)
  if y == 0:
    y = h
  y = str(y)
  result = y+x
  list.append(result)

for i in range(t):
  print(list[i])