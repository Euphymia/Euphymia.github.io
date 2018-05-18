#50 Pow(x, n)

---

> * 问题
> * 代码
> * 思路
> * time.clock()的使用方法

---

## 问题

实现 pow(x, n) ，即计算 x 的 n 次幂函数。

示例 1:

输入: 2.00000, 10

输出: 1024.00000

示例 2:

输入: 2.10000, 3

输出: 9.26100

示例 3:

输入: 2.00000, -2

输出: 0.25000

解释: 2-2 = 1/22 = 1/4 = 0.25

说明:

-100.0 < x < 100.0

n 是 32 位有符号整数，其数值范围是[−231, 231 − 1] 。

## 代码

```python
import time
class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n >= 0:
            return self.power(x, n)
        else:
            return 1/self.power(x, -n)

    def power(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        temp=self.power(x,n//2)
        if n % 2 == 0:
            return temp**2
        else:
            return x*temp**2


def test():
    sl = Solution()
    return sl.myPow(23, 3648)


def test2():
    return 23 ** 3648


if __name__ == '__main__':
    while True:
        time_start = time.clock()
        test()
        time_end = time.clock()
        shift_time = time_end - time_start
        print(shift_time)
        time_start2 = time.clock()
        test2()
        time_end2 = time.clock()
        shift_time2 = time_end2 - time_start2
        print("test2",shift_time2)
        # print(shift_time >= shift_time2)
```

## 思路

只用分治法处理x的n次幂问题。

##time.clock()的使用方法

```
Python time clock() 函数以浮点数计算的秒数返回当前的CPU时间。用来衡量不同程序的耗时，比time.time()更有用。

这个需要注意，在不同的系统上含义不同。在UNIX系统上，它返回的是"进程时间"，它是用秒表示的浮点数（时间戳）。而在WINDOWS中，第一次调用，返回的是进程运行的实际时间。而第二次之后的调用是自第一次调用以后到现在的运行时间。（实际上是以WIN32上QueryPerformanceCounter()为基础，它比毫秒表示更为精确）
```

