import sys
n = int(sys.stdin.readline().rstrip())
numbers = [0] * 301
store = [0] * 301

for i in range(n):
  numbers[i] = int(sys.stdin.readline().rstrip())

store[0] = numbers[0]
store[1] = numbers[0] + numbers[1]
store[2] = max(numbers[0]+numbers[2], numbers[1]+numbers[2])
for i in range(3, n):
  store[i] = max(numbers[i]+store[i-2], numbers[i]+numbers[i-1]+store[i-3])

print(store[n-1])