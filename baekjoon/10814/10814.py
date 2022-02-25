import sys
n = int(sys.stdin.readline().rstrip())
people = []

for i in range(n):
  temp = list(sys.stdin.readline().rstrip().split(" "))
  temp.append(i)
  temp[0] = int(temp[0])
  people.append(temp)

people.sort(key = lambda x: (x[0], x[2]))

for i in range(n):
  print(people[i][0], people[i][1])