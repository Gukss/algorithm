t = int(input())

def Prime(n):
  list = [True] * (n+1)
  for i in range(2, int(n**0.5) + 1):
    if list[i]:
      for j in range(i+i, n+1, i):
        list[j] = False
  return list

def check(n, list):
  temp = []
  for i in range(n, 1, -1):
    if list[i]:
      temp.append(i)
  for i in range(n//2, 1, -1):
    if list[i]:
      for j in temp:
        if (j+i == n):
          return i, j

for i in range(t):
  n = int(input())
  list = Prime(n)
  num1, num2 = check(n, list)
  print(str(num1) + " " + str(num2))

