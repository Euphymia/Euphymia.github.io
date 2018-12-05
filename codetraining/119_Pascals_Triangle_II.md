#119_Pascals_Triangle_II

------

> - 问题
> - 代码
> - 思路

------

## 问题

 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。

 

在杨辉三角中，每个数是它左上方和右上方的数的和。

[

​     [1],

​    [1,1],

   [1,2,1],

  [1,3,3,1],

 [1,4,6,4,1]

]

示例:

 

输入: 3

输出: [1,3,3,1]

## 代码

```python
class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex==0:
            return [1]
        last_level=[1]
        length=1
        for i in range(1,rowIndex+1):
            length+=1
            new_level=[]
            for i in range(length):
                if 0< i <length-1 :
                    new_level.append(last_level[i-1]+last_level[i])
                elif i == length-1:
                    new_level.append(last_level[-1])
                else:
                    new_level.append(last_level[0])
            last_level=new_level
        return last_level

if __name__ == "__main__":  
    sl=Solution()
    rowIndex=6
    print(sl.getRow(rowIndex))

```

## 思路

思路：

与118题很像，不需要保存进res中，返回最后一行创建的数组即可。