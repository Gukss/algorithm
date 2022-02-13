testCase = int(input())

for i in range(testCase):
  a, b = map(int, input().split(" "))
  count = 0
  distance = b - a
  move = 1
  sum_move = 0
  while (distance > sum_move):
    count += 1
    sum_move += move
    if (count % 2 == 0):
      move += 1
  print(count)
