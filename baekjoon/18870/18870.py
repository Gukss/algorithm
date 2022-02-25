import sys
n = int(sys.stdin.readline().rstrip())
numbers = []

numbers = list(map(int, sys.stdin.readline().rstrip().split(" ")))

result = list(set(numbers))
result.sort()

dic = { result[i] : i for i in range(len(result))}

for i in range(n):
  sys.stdout.write(str(dic[numbers[i]]) + " ")