# 백준 2775번

## 부녀회장이 될테야

---

```python
result = []
```

> 결과를 저장할 result 리스트

---

```python
def check():
  global result
  t = int(input())
```

> 함수 check안에서 실행한다.  
> result를 전역변수로 만들어준다.  
> test case 수를 입력받는 변수 t.

---

```python
  for num in range(t):
    k = int(input())
    n = int(input())

    count = 0
    list=[]
    newList = []
```

> t 만큼 반복한다.  
> k와 n을 따로 입력받는다.  
> 누적 합을 저장할 count 변수, 아래 층의 값을 저장할 list 변수와 현재 층의 값을 저장할 newList 변수를 초기화 한다.

---

```python
		for i in range(n):
			list.append(i+1)
```

> 위의 for문 안에서 실행된다.  
> n호의 값을 찾으면 되기 때문에 0층의 값을 인덱스 n 까지만 초기화 한다.  
> range(n) for문은 여기까지

---

```python
		for i in range(k):
			for j in range(n):
				count+=list[j]
				newList.append(count)
			list = newList.copy()
			newList.clear()
		count = 0
```

> k층의 값을 찾기위해 n번 반복한다.  
> n호의 값을 찾기위해 n번 반복한다.  
> 누적 값을 저장하는 count에 list[i]값을 저장하고 newList에 추가해 준다.  
> j가 하나씩 증가할 때 마다 i층 j호의 값이 newList에 저장된다.  
> range(n) for문을 완료하고 newList의 값을 list로 복사한다.  
> newList를 초기화하고 반복문을 탈출하면 다음 test case를 위해 count를 초기화 한다.

---

```python
    result.append(list[n - 1])

check()
for i in result:
  print(i)
```

> list[n - 1]에 원하는 답이 담겨있다. result에 추가한다.  
> result의 값을 출력한다.
