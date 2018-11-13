#935_Knight_Dialer

------

> - 问题
> - 代码
> - 思路

------

## 问题

 935.骑士拨号器

国际象棋中的骑士可以按下图所示进行移动：

![](/935_Knight_Dialer1.png)

![](/935_Knight_Dialer2.png)

这一次，我们将 “骑士” 放在电话拨号盘的任意数字键（如上图所示）上，接下来，骑士将会跳 N-1 步。每一步必须是从一个数字键跳到另一个数字键。

每当它落在一个键上（包括骑士的初始位置），都会拨出键所对应的数字，总共按下 N 位数字。

你能用这种方式拨出多少个不同的号码？

因为答案可能很大，所以输出答案模 10^9 + 7。

示例 1：

输入：1

输出：10

示例 2：

 

输入：2

输出：20

示例 3：

输入：3

输出：46

提示：

 

1 <= N <= 5000

## 代码

```python
class Solution(object):
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 1:
            return 10
        dic = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }

        table = [1] * 10
        while N > 1:
            next_table = [0] * 10
            for i in range(10):
                for j in dic[i]:
                    next_table[j] += table[i]
            table = next_table
            N -= 1
        return sum(table) % (10 ** 9 + 7)


if __name__=="__main__":
    sl=Solution()
    print(sl.knightDialer(3))
```

## 思路

思路:

思路很好，初始化可能跳转的号码dic，精妙的地方在于，table,初始化为全1，这是N为1的情况，再后面对N>1开始遍历时，每次遇到可能跳转的号码

执行next_table[j] += table[i]，这样可以应对某个号码被多次转到的情况。