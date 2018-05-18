#03 super prime

---

> * 问题
> * 代码
> * 思路

---

##问题

实现一种改进的素数识别方法。打印1-1000以内的所有素数

## 代码

```python
def isprime(num):
    if num%2==0:
        return num==2
    elif num%3==0:
        return num==3
    elif num%5==0:
        return num==5
    i=2
    while i*i<=num:
        if num%i==0:
            return False
        i+=1
    return True
count=0
for i in range(2,1000):
    if isprime(i):
        print(i)
        count+=1
print(count)
```

## 思路

先判别能否整除2,3,5这几个常见因子，为了避免漏掉2,3,5在判断能整除后返回num==2的结果。在循环中使用i*i<num作为结束条件，一是可以减少循环次数(i<sqrt(num))而是可以加速计算,乘法往往比开根号快