#51 N-Queens

---

> * 问题
> * 代码
> * 思路
> * 间接修改字符串中字符的方法

---

## 问题 

n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。

每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

示例:

输入: 4

输出: 

[

[".Q..",  // 解法 1

"...Q",

"Q...",

"..Q."],

["..Q.",  // 解法 2

"Q...",

"...Q",

".Q.."]

]

解释: 4 皇后问题存在两个不同的解法。

## 代码

```python
class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res=[]
        pos=[-1]*n
        self.solveNQueensDFS(res,pos,0)
        return res
    def solveNQueensDFS(self,res,pos,row):
        n=len(pos)
        if row==n:
            out=['.'*n]*n
            for i in range(n):
                newlist=list(out[i])
                newlist[pos[i]]="Q"
                newlist="".join(newlist)
                out[i]=newlist
            res.append(out)
            return 
        for col in range(0,n):
            if self.isvalid(col,row,pos):
                pos[col]=row
                self.solveNQueensDFS(res,pos,row+1)
                pos[col]=-1

        
    def isvalid(self,col,row,pos):
        if pos[col]!=-1:
            return False
        for i in range(1,row+1):
            if (col-i)>=0 and pos[col-i]==row-i:
                return False
            if (col+i)<len(pos) and pos[col+i]==row-i:
                return False
        return True
def test():
    sl=Solution()
    res=sl.solveNQueens(4)
    print(res)
    print(len(res))

if __name__=='__main__':
    test()
```

## 思路

思路：经典的N皇后问题，基本所有的算法书中都会包含的问题，经典解法为回溯递归，一层一层的向下扫描，需要用到一个pos数组，其中pos[i]表示第i行皇后的位置，初始化为-1，然后从第0开始递归，每一行都一次遍历各列，判断如果在该位置放置皇后会不会有冲突，以此类推，当到最后一行的皇后放好后，一种解法就生成了，将其存入结果res中，然后再还会继续完成搜索所有的情况

判断新放入的位置是否冲突是重点，即斜方向和垂直方向都不能有棋子。这里判断新位置左上方向和右上方向两个方向上是否存在棋子

##间接修改字符串中字符的方法

```python
方法一：将字符串转换为列表，修改列表的元素后，在重新连接为字符串:

str1 = "string"
str2 = list(str1)    #将字符串转换为列表，列表的每一个元素为一个字符
str2[2] = 'x' 
str2 = ''.join(str2)     #将列表重新连接为字符串
print(str1,str2)
>>>string stxing
方法二：使用str.replace方法替换成我们想要的字符串，replace函数用法：str.replace(old, new, max)，是把字符串str中的所有old字符子串替换为new，max指定从左往右的最大替换次数，max可省略。

str1 = "string"
str2 = str1.replace(str1[2],'x')    #将字符串第三位替换为x
print(str1,str2)
>>>string stxing

方法三：将字符串切片后相加：

str1 = "string"
str2 = str1[0:2]+'x'+str1[3:]   #先切后合
print(str1,str2)
>>>string stxing
```

