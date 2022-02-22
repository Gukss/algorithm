import sys
n = sys.stdin.readline().rstrip()
numbers = []

for i in n:
  numbers.append(i)

numbers.sort(reverse = True)
for i in numbers:
  sys.stdout.write(i)