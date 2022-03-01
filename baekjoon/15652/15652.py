import sys
n, m = map(int, sys.stdin.readline().rstrip().split(" "))
numbers = []

def dfs(a):
  if len(numbers) == m:
    print(' '.join(map(str, numbers)))
    return
  for i in range(a, n+1):
    numbers.append(i)
    dfs(i)
    numbers.pop()

dfs(1)