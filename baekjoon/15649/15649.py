import sys
n, m = map(int, sys.stdin.readline().rstrip().split(" "))
numbers = []

def dfs():
  if len(numbers) == m:
    print(' '.join(map(str, numbers)))
    return
  for i in range(1, n+1):
    if i not in numbers:
      numbers.append(i)
      dfs()
      numbers.pop()

dfs()