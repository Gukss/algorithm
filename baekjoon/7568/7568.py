n = int(input())
people = []
result = ""
for i in range(n):
  people.append(list(map(int, input().split(" "))))

for i in range(n):
  count = 1
  for j in range(n):
    if (people[i][0] < people[j][0]) & (people[i][1] < people[j][1]):
      count += 1
  result = result + str(count) + " "

print(result)