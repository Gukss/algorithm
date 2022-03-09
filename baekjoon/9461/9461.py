import sys
t = int(sys.stdin.readline().rstrip())
numbers = [0] * 101
numbers[0] = 1
numbers[1] = 1
numbers[2] = 1
numbers[3] = 2
numbers[4] = 2

def check(n):
  for i in range(n):
    if numbers[i]:
      continue
    numbers[i] = (numbers[i-1] + numbers[i-5])

for i in range(t):
  n = int(sys.stdin.readline().rstrip())
  check(n)
  print(numbers[n-1])