# 백준 1065번

## 한수

---

```python

```

> num에 입력값 저장, count에 한수의 개수를 저장한다.

> 1에서 입력한 숫자까지 반복하며 한수를 찾는 함수 han을 실행한다.

> num이 100보다 작으면 `count++` 한다. 무조건 한수다.

> num을 문자열로 바꿔 list에 저장한다.

> 문자열의 길이만큼 반복한다. 인덱스 `i+2` 까지 확인해야 하므로 `len(list)-2` 해준다.

> diff1에 첫 번째 숫자와 두 번째 숫자의 차이를 저장하고 diff2에 두 번째 숫자와 세 번째 숫자의 차이를 저장한다.  
> diff1과 diff2가 다르면 `return`한다.

> 반복문을 모두 통과하면 `count++`한다.
