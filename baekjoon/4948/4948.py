def isPrime(n):
  list=[]
  count = 0
  for i in range(2*n + 1):
    list.append(i)
  list[1] = 0
  for i in range(2, 2*n + 1):
    if list[i] == 0:
      continue
    for num in range(i+i, 2*n + 1, i):
      list[num] = 0
  for i in range(n+1, 2*n + 1):
    if list[i] != 0:
      count += 1
  print(count)


while True:
  n = int(input())
  count = 0
  if n == 0:
    break
  isPrime(n)

