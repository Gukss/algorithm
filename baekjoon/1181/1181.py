import sys
n = int(sys.stdin.readline().rstrip())
words = []

for i in range(n):
  word = sys.stdin.readline().rstrip()
  length = len(word)
  words.append([word, length])

words = list(set(map(tuple, words)))

words.sort(key = lambda x: (x[1], x[0]))

for i in words:
  print(i[0])