import sys
n = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().rstrip().split(" ")))
opt = list(map(int, sys.stdin.readline().rstrip().split(" ")))
val = []
result = []
maxi = -1e9
mini = 1e9

def dfs(depth, total, plus, minus, multiply, divide):
  global maxi, mini
  if depth == n:
    maxi = max(total, maxi)
    mini = min(total, mini)
    return
  
  if plus:
    dfs(depth+1, total + numbers[depth], plus - 1, minus, multiply, divide)
  if minus:
    dfs(depth+1, total - numbers[depth], plus, minus - 1, multiply, divide)
  if multiply:
    dfs(depth+1, total * numbers[depth], plus, minus, multiply - 1, divide)
  if divide:
    dfs(depth+1, int(total / numbers[depth]), plus, minus, multiply, divide - 1)


dfs(1, numbers[0], opt[0], opt[1], opt[2], opt[3])
print(maxi)
print(mini)