m, n = map(int, input().split(" "))

board = []
count = []

for i in range(m):
  board.append(input())

for i in range(m-7):
  for j in range(n-7):
    idx1 = 0 # w로 시작
    idx2 = 0 # b로 시작
    
    for a in range(i, i+8):
      for b in range(j, j+8):
        if (a+b) % 2 == 0:
          if board[a][b] == 'B':
            idx1 += 1
          else:
            idx2 += 1
        else:
          if board[a][b] == 'W':
            idx1 += 1
          else:
            idx2 += 1
    count.append(min(idx1, idx2))

print(min(count))
