import sys
n = int(sys.stdin.readline().rstrip())
numbers = []

for i in range(n):
  numbers.append(list(map(int, sys.stdin.readline().rstrip().split(" "))))

k = 2
for i in range(1, n):
  for j in range(k):
    if j == 0:
      numbers[i][j] += numbers[i-1][j]
    elif i==j:
      numbers[i][j] += numbers[i-1][j-1]
    else:
      numbers[i][j] += max(numbers[i-1][j], numbers[i-1][j-1])
  k += 1

print(max(numbers[n-1]))