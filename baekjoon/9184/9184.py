import sys
def dfs(a, b, c):
  if a <= 0 or b <= 0 or c <= 0:
    return 1
  if a > 20 or b > 20 or c > 20:
    return dfs(20, 20, 20)
  if board[a][b][c]:
    return board[a][b][c]
  if a < b and b < c:
    board[a][b][c] = dfs(a, b, c-1) + dfs(a, b-1, c-1) - dfs(a, b-1, c)
    return board[a][b][c]
  board[a][b][c] = dfs(a-1, b, c) + dfs(a-1, b-1, c) + dfs(a-1, b, c-1) - dfs(a-1, b-1, c-1)
  return board[a][b][c]

board = [[[None for x in range(21)] for y in range(21)] for z in range(21)]

while(True):
  a, b, c = map(int, sys.stdin.readline().rstrip().split(" "))
  if a==-1 and b==-1 and c==-1:
    break
  print('w({0}, {1}, {2}) = {3}'.format(a, b, c, dfs(a, b, c)))