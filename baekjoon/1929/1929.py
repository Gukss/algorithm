m, n = map(int, input().split(" "))
list = []
for i in range(n+1):
  list.append(i)

for num in range(2, n+1):
  if list[num] == 0:
    continue
  for i in range(num + num, n+1, num):
    list[i] = 0

for i in range(m, n+1):
  if list[i] != 0:
    print(list[i])