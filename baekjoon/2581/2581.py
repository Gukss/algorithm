m = int(input())
n = int(input())
list = []

for num in range(m, n+1):
  prime = 1
  if num == 1:
    prime = 0
  for i in range(2, num):
    if num % i == 0:
      prime = 0
      break
  if prime == 1:
    list.append(num)


if len(list) == 0:
  print(-1)
else:
  print(sum(list))
  print(list[0])