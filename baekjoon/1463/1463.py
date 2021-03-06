import sys
n = int(sys.stdin.readline().rstrip())

count = [0]*(n+1)

for i in range(2, n+1):
  count[i] = count[i-1] + 1
  if (i+3) % 3 == 0:
    count[i] = min(count[int(i//3)] + 1, count[i])
  if (i+2) % 2 == 0:
    count[i] = min(count[int(i//2)] + 1, count[i])

print(count[n])