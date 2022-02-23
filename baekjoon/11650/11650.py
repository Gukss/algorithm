import sys
n = int(sys.stdin.readline().rstrip())

pos = []
for i in range(n):
  pos.append(list(map(int, sys.stdin.readline().rstrip().split(" "))))

pos.sort(key = lambda x: (x[0], x[1]))

for i in pos:
  print(i[0], i[1])