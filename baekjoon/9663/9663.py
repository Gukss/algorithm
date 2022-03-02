import sys
n = int(sys.stdin.readline().rstrip())
board = [0] * 15
result = 0

def check(x):
  for i in range(x):
    if (board[x] == board[i]) | (abs(board[x] - board[i]) == abs(x - i)):
      return False
  return True

def n_queens(x):
  global result
  if x == n:
    result += 1
    return
  else:
    for i in range(n):
      board[x] = i
      if check(x):
        n_queens(x+1)

n_queens(0)
print(result)
