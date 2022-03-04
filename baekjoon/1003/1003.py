import sys
t = int(sys.stdin.readline().rstrip())
zero = [1, 0]
one = [0, 1]

def fibo(n):
  len_zero = len(zero)
  if len_zero <= n:
    for i in range(len_zero, n+1):
      zero.append(zero[i-1] + zero[i-2])
      one.append(one[i-1] + one[i-2])
  print(zero[n], one[n])

for i in range(t):
  fibo(int(sys.stdin.readline().rstrip()))
