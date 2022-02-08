# 백준 2292번

## 벌집

---

```python
num = int(input())

def check(num):
  if(num ==1):
    print(1)
    return
  num = num-2
  count = 1
  while(num >= 0):
    num = num - (count * 6)
    count += 1
  print(count)

check(num)
```

> input num을 매개변수로 하는, 몇 개의 방을 지나가는지 계산하는 함수 check

> 규칙  
> [1] - 1개 방 - 1개  
> [2, 7] - 2개 방 - 6개  
> [8, 19] - 3개 방 - 12개  
> [20, 37] - 4개 방 - 18개

> 1을 입력받으면 1을 출력하고 `return`

> `num == 1`일 때를 제외하고 `num = num - 2`하면  
> 범위가  
> [0, 5]  
> [6, 17]  
> [18, 35]  
> 로 변한다.

> 하위 범위에 속해 있으면 `num = num - (count * 6)` 하면 num이 음수가 돼 반복문을 탈출한다.

> ex ) `num == 11`일 때 `count == 1`  
> iter1: `num == 5` `count == 2`: num이 양수이므로 반복문 진행한다.
> iter2: `num == -7` `count == 3`: num이 음수이므로 반복문 탈출한다.
> count가 문제의 답이다.
