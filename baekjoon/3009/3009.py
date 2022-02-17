list = []
result = []

for i in range(3):
  list.append(input().split(" "))

for i in range(2):
  if (list[0][i] != list[1][i]) & (list[0][i] != list[2][i]):
    result.append((list[0][i]))
  if (list[0][i] != list[1][i]) & (list[0][i] == list[2][i]):
    result.append((list[1][i]))
  if (list[1][i] != list[2][i]) & (list[0][i] == list[1][i]):
    result.append((list[2][i]))

print(result[0] + " " + result[1])
	
