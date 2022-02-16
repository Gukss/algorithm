m, n = map(int, input().split(" "))

for i in range(m, n+1):
  if i == 1:
    continue
  prime = 1
  for num in range(2, int(i**0.5) + 1):
    if i % num == 0:
      prime = 0
      break
  if prime == 1:
    print(i)