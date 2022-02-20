import sys

n = int(input())
numbers = []

for i in range(n):
  numbers.append(int(sys.stdin.readline()))

for i in sorted(numbers):
  sys.stdout.write(str(i) + "\n")