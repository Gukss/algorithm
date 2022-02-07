# 백준 1316번

## 그룹 단어 체커

---

if 중첩을 고친 코드

```python
num = int(input())
count = 0

def check(string):
alph = [1 for i in range(26)]
global count
for i in range(len(string) - 1):
text = string[i]
if (text == string[i+1]):
continue
if(alph[ord(text) - 97] == 0):
return
alph[ord(text) - 97] = 0
if(alph[ord(string[i+1]) - 97] == 0):
return
count += 1

for i in range(num):
string = input()
check(string)

print(count)
```

> 1. 단어 개수만큼 check 함수를 반복한다.
> 2. check 함수는 입력된 문자열을 매개변수로 하는 함수이다.
> 3. 알파벳의 총 개수는 26개, 크기가 26이고 모두 1로 채워진 리스트 alph를 선언한다.  
>    함수 안에 선언해 반복문이 반복될 때 마다 새로 선언되도록 한다.  
>    한 번 나왔던 문자가 중복해서 나오는지 확인할 용도이다.
> 4. 문자열 길이만큼 반복한다.  
>    다음 문자와 비교하는 `string[i+1]`에서 인덱스가 문자열 길이를 벗어나지 않도록 범위를 `range(len(string) - 1)`로 지정해 준다.
> 5. 첫 번째 if: 현재 문자와 다음 문자가 같으면 `continue`해 반복문을 진행시킨다.
> 6. 두 번째 if: 현재 문자가 한 번 이상 나온 문자면 `return`
> 7. 세 번째 if 위 `alph[ord(text) - 97] = 0` 현재 문자와 다음 문자가 다르고 현재 문자가 한 번도 나오지 않은 문자면 `alph[ord(text) - 97] = 0`, 문자가 한 번 이상 나왔다고 표시한다.
> 8. 세 번째 if: 다음 문자가 한 번 이상 나온 문자면 `return`, 제일 마지막 문자를 검사한다.
> 9. for문이 무사히 종료되면 `count+=1` 한다.

if 중첩 고치기 전 코드

```python
num = int(input())
count = 0

def check(string):
  alph = [1 for i in range(26)]
  global count
  for i in range(len(string) - 1):
    text = string[i]
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
```
