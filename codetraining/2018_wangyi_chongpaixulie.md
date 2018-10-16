#重排数列 

------

> - 问题
> - 代码
> - 思路

## 问题

重排数列

小易有一个长度为N的正整数数列A = {A[1], A[2], A[3]..., A[N]}。

牛博士给小易出了一个难题:

对数列A进行重新排列, 使数列A满足所有的A[i] * A[i + 1](1 ≤ i ≤ N - 1)都是4的倍数。

小易现在需要判断一个数列是否可以重排之后满足牛博士的要求。

输入描述:

输入的第一行为数列的个数t(1 ≤ t ≤ 10),

接下来每两行描述一个数列A, 第一行为数列长度n(1 ≤ n ≤ 10 ^ 5)

第二行为n个正整数A[i](1 ≤ A[i] ≤ 10 ^ 9)

 

 

输出描述:

对于每个数列输出一行表示是否可以满足牛博士要求, 如果可以输出Yes, 否则输出No。

 

输入例子1:

2

3

1 10 100

4

1 2 3 4

 

输出例子1:

Yes

No

## 代码

```python

count=int(input())
res=[]
while count>0:
    fourcount=0
    twocount=0
    onecount=0
    num=int(input())
    str1=input()
    str1list=str1.split(" ")
    numlist=[int(i) for i in str1list]
    for i in numlist:
        if i%4==0:
            fourcount+=1
            continue
        if i%2==0:
            twocount=1
            continue
        onecount+=1
    if fourcount>=onecount+twocount-1:
        res.append('Yes')
    else:
        res.append('No')
        
    count-=1


for i in res:
    print(i)

```

## 思路

记录输入的数组中包含的能整除4,2以及不能这些整除的个数。

其中不管有多少能被2整除，个数都记为1，以为将他们连起来排列可视为一个不能2,4整除的数。

只要fourcount >= onecount+twocount-1，就存在这种排列

