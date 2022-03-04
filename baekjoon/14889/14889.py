import sys
n = int(sys.stdin.readline().rstrip())
member = int(n/2)
select = [0 for i in range(n)]

board = []
for i in range(n):
  board.append(list(map(int, sys.stdin.readline().rstrip().split(" "))))

ans = sys.maxsize

def dfs(idx, count):
  global ans
  if count == member:
    start, link = 0, 0
    for i in range(n):
      for j in range(n):
        if select[i] and select[j]:
          start += board[i][j]
        elif not select[i] and not select[j]:
          link += board[i][j]
    ans = min(ans, abs(start - link))
    return

  for i in range(idx, n):
    if select[i] == 1:
      continue
    select[i] = 1
    dfs(i+1, count+1)
    select[i] = 0

dfs(0, 0)
print(ans)