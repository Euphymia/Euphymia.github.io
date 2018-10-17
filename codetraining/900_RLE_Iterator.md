#900_RLE_Iterator

------

> - 问题
> - 代码
> - 思路

## 问题

900.RLE 迭代器

 

编写一个遍历游程编码序列的迭代器。

 

迭代器由 RLEIterator(int[] A) 初始化，其中 A 是某个序列的游程编码。更具体地，对于所有偶数 i，A[i] 告诉我们在序列中重复非负整数值 A[i + 1] 的次数。

 

迭代器支持一个函数：next(int n)，它耗尽接下来的  n 个元素（n >= 1）并返回以这种方式耗去的最后一个元素。如果没有剩余的元素可供耗尽，则  next 返回 - 1 。

 

例如，我们以 A = [3, 8, 0, 9, 2, 5] 开始，这是序列[8, 8, 8, 5, 5] 的游程编码。这是因为该序列可以读作 “三个八，零个九，两个五”。

 

 

示例：

 

输入：["RLEIterator", "next", "next", "next", "next"], [[[3, 8, 0, 9, 2, 5]], [2], [1], [1], [2]]

输出：[null, 8, 8, 5, -1]

解释：

RLEIterator 由 RLEIterator([3, 8, 0, 9, 2, 5]) 初始化。

这映射到序列[8, 8, 8, 5, 5]。

然后调用 RLEIterator.next 4次。

 

.next(2) 耗去序列的 2 个项，返回 8。现在剩下的序列是[8, 5, 5]。

 

.next(1) 耗去序列的 1 个项，返回 8。现在剩下的序列是[5, 5]。

 

.next(1) 耗去序列的 1 个项，返回 5。现在剩下的序列是[5]。

 

.next(2) 耗去序列的 2 个项，返回 - 1。 这是由于第一个被耗去的项是 5，

但第二个项并不存在。由于最后一个要耗去的项不存在，我们返回 - 1。

 

 

提示：

 

0 <= A.length <= 1000

A.length 是偶数。

0 <= A[i] <= 10 ^ 9

每个测试用例最多调用 1000 次 RLEIterator.next(int n)。

每次调用 RLEIterator.next(int n) 都有 1 <= n <= 10 ^ 9 。

题目大意：

输入两个数组第一个数组中，偶数位表示后面一位奇数位数组的个数。

第二个数组表示，删除由第一个数组构成的新数组的前x项，并输出删除的最后一个数，如果删除完了则返回-1.

## 代码

```python
class RLEIterator:
    
    def __init__(self, A):
        """
        :type A: List[int]
        """
        # [3, 8, 0, 9, 2, 5]
        i=0
        self.data=[]
        self.count=[]
        while i<len(A):
            if i%2==0:
                self.data.append(A[i+1])
                self.count.append(A[i])
            i+=1
        
    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        countsum=sum(self.count)
        if n>=countsum:
            self.count=[]
            return -1
        elif n<self.count[0]:
            self.count[0]-=n
            return self.data[0]
        # elif n==self.count[0]:
        #     self.count.pop(0)
        #     return self.data.pop(0)
        else:
            while n-self.count[0]>0:
                n-=self.count[0]
                self.count.pop(0)
                self.data.pop(0)
            if n==self.count[0]:
                self.count.pop(0)
                return self.data.pop(0)
            self.count[0] -= n
            return self.data[0]

if(__name__=='__main__'):
    A=[int(i) for i in input()[1:-1].split(',')]
    B = [int(i) for i in input()[1:-1].split(',')]
    obj = RLEIterator(A)
    for i in B:
        print(obj.next(i))
    # param_1 = obj.next(B)



# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)
# 测试案例
# [811, 903, 310, 730, 899, 684, 472, 100, 434, 611]
# [358,345,154,265,73,220,138,4,170,88]
```

## 思路

思路很明确，首先不能真的保存初始化的数组，这里使用count[]，和data[]两个数组记录初始化的数据。

然后开始查询，如果查询的数大于count的所有数的和，则直接返回-1，并将count置零，否则，如果大于count[0]则一直向下找小于count[0]的值，最后返回对应的data[0]，

如果遇到等于count[0]，依旧返回对应的data[0]，循环即可。