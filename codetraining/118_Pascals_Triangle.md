#118_Pascals_Triangle

------

> - 问题
> - 代码
> - 思路

------

## 问题

 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。

 

在杨辉三角中，每个数是它左上方和右上方的数的和。

 

示例:

 

输入: 5

输出:

[

​     [1],

​    [1,1],

   [1,2,1],

  [1,3,3,1],

 [1,4,6,4,1]

]

## 代码

```python
class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res=[[1]]
        if numRows==1:
            return res
        elif numRows==0:
            return []
        last_level=[1]
        length=1
        for i in range(1,numRows):
            length+=1
            new_level=[]
            for i in range(length):
                if i == 0 :
                    new_level.append(last_level[0])
                elif i == length-1:
                    new_level.append(last_level[-1])
                else:
                    new_level.append(last_level[i-1]+last_level[i])
            res.append(new_level)
            last_level=new_level
        return res
if __name__ == "__main__":  
    sl=Solution()
    numRows=5
    print(sl.generate(numRows))
```

## 思路

思路：

很简单，根据循环，创建每行的一个新数组，数组的元素是前一行数组对应位置的和，最后添加到res中即可。