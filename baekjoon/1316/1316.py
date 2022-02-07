num = int(input())
count = 0

def check(string):
  alph = [1 for i in range(26)]
  global count
  # 문자열 길이만큼 반복
  for i in range(len(string) - 1):
    text = string[i]
    # 다음 문자가 현재 문자랑 다르면 0으로 바꾸고
    if (text != string[i+1]):
      if(alph[ord(text) - 97] == 1):
        alph[ord(text) - 97] = 0
        if(alph[ord(string[i+1]) - 97] == 0):
          return
      elif(alph[ord(text) - 97] == 0):
        return
  count += 1
  
for i in range(num):
  string = input()
  check(string)

print(count)