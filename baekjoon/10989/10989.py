import sys

n = int(sys.stdin.readline())
# numbers = [0] * n 으로 실패
numbers = [0] * 10001

for _ in range(n):
  numbers[int(sys.stdin.readline())] += 1

for i in range(1, 10001):
    for _ in range(numbers[i]):
      print(i)