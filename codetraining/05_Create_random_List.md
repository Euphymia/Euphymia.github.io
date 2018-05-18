##05 Create random List

---

> * 问题
> * 代码
> * 思路

---

## 问题

产生一个1-N的M个不重复随机整数数列，其中M>=N

## 代码

```python
import random
import time
def createRandomList(n,m):
    source=list(range(1,m+1))
    res=[]
    for i in range(n):
        out=random.randint(0,m-1)
        res.append(source[out])
        source[out],source[m-1]=source[m-1],source[out]
        m-=1
    return res
starttime=time.clock()
res=createRandomList(8,10)
endtime=time.clock()
print(res)
print(endtime-starttime)
```

## 思路

这个算法与一般的判断随机出来的数是否在res中，再加入res相比有很大的改进。

首先建立一个1到M的源列表，然后通过随机下标的方式，挑选随机数。为了避免存在重复，每次随机一个1到m的下标out后，把out对应的数据存入res，交换源列表中out位置的数与最后一个数交换位置。将m自减,进入下一次循环