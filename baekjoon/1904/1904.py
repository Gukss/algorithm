import sys
n = int(sys.stdin.readline().rstrip())
count = 0
board = [0] * 1000001
board[1] = 1
board[2] = 2

def dfs(n):
  for i in range(3, n+1):
    board[i] = int((board[i-1] + board[i-2]) % 15746)

dfs(n)
print(board[n])
