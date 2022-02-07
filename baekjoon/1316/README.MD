# 백준 1316번

## 그룹 단어 체커

---

{% highlight python linenos %}
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
{% endhighlight %}
