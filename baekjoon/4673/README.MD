# 백준 4673번

## 셀프 넘버

---

```python
list1 = []
for i in range(10000):
    list1.append(i+1)

list2 = []

def selfNum(list2, n):
    num = n
    for i in range(len(str(n))):
        num += (n % 10)
        n = int(n / 10)
    if(num > 10000):
        return
    list2.append(num)
    return

for i in range(10000):
    selfNum(list2, i+1)

a = [x for x in list1 if x not in list2]
for i in a:
    print(i)
```

> 10000 까지 숫자를 가진 리스트 list1

> 1에서 10000 까지 반복하면서 셀프 넘버 검사하는 함수 selfNum를 실행한다.

> num에 셀프 넘버인지 검사하려는 숫자를 저장한다.

> 숫자를 문자열로 변경해 길이 만큼 반복한다.  
> ex ) 숫자가 100이면 3번 반복한다.

> num에 10으로 나눈 나머지인 1의자리 숫자를 더한다.

> n을 10으로 나눠 n에서 1의 자리를 뺀다.

> num이 10000을 넘어가면 문제에서 원하는 출력이 나오지 않는다.

> list2에 셀프넘버가 아닌, 생성자가 있는 num을 추가해 준다.

> `a = [x for x in list1 if x not in list2]`  
> a에 list1에서 list2를 뺀 리스트, list1에서 list2에 없는 것만 a에 저장한다. (리스트 빼기, 리스트 차집합, 리스트 컴프리헨션)
