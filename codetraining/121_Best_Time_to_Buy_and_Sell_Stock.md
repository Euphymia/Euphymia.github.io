#121_Best_Time_to_Buy_and_Sell_Stock

------

> - 问题
> - 代码
> - 思路

------

## 问题

 121.买卖股票的最佳时机

 

给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

 

如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

 

注意你不能在买入股票前卖出股票。

 

示例 1:

 

输入: [7,1,5,3,6,4]

输出: 5

解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。

​     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。

示例 2:

 

输入: [7,6,4,3,1]

输出: 0

解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

## 代码

```python

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res=0
        if not prices:
            return 0
        i=1
        stack=[prices[0]]
        while i<len(prices):
            while i<len(prices)-1 and stack[-1]>prices[i]:
                stack.append(prices[i])
                i+=1
            res=max(res,prices[i]-stack[-1])
            i+=1
        return res

    

if __name__ == "__main__":
    sl=Solution()
    prices=[7,1,5,3,6,4]
    print(sl.maxProfit(prices))
```

## 思路

思路：

想法还行，刚开始就想到了使用单调栈模型，但是中间出了点问题，好像不适用，就稍微改了一下。

首先创建一个最大的整数值用于保存当前遇到的最小值，和一个单调栈。

遇到栈空或者一个小值则入站，遇到大的值，将stack中小的值依次出栈，并更新当前最小的值cur_min，用于更新结果res=max(res,i-cur_min)，

cur_min就是起到了一个保存最小值的作用，不然的话，遇到大的值不能与之前已经出现过的小值比较了。