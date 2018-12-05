#943_Find_the_Shortest_Superstring

------

> - 问题
> - 代码
> - 思路

------

## 问题

 \943. 最短超级串

 

给定一个字符串数组A，找出一个字符串S使得A中的每个字符串都是S的一个子串，并且使S的长度最短。

 

默认A中不存在某一个字符串是另一个字符串的子串。

示例 1：

 

输入：["alex","loves","leetcode"]

输出："alexlovesleetcode"

解释："alex"，"loves"，"leetcode" 的所有排列都会被接受。

示例 2：

 

输入：["catg","ctaagt","gcta","ttca","atgcatc"]

输出："gctaagttcatgcatc"

 

 

提示：

 

1 <= A.length <= 12

1 <= A[i].length <= 20

## 代码

```python
import itertools
class Solution:
    def shortestSuperstring(self, A):
        def merge(a, b):
            for i in range(len(b), 0, -1):
                if a.endswith(b[:i]):
                    return i
            return 0
        def dfs(sup, s, st):
            if len(sup + "".join(st)) < len(res[0]):
                res[0] = sup + "".join(st)
            if st and any(new in st for new in merged[s][1:]):
                for new in merged[s][1:]:
                    if new in st:
                        dfs(sup + new[merged[s][0]:], new, st - {new})
            else:
                for nex in st:
                    for new in merged[nex][1:]:
                        if new in st:
                            dfs(sup + nex + new[merged[nex][0]:], new, st - {nex, new})
        merged, res = {}, ["".join(A)]
        for a, b in itertools.combinations(A, 2):
            for a, b in ((a, b), (b, a)):
                l = merge(a, b)
                if a not in merged or l > merged[a][0]:
                    merged[a] = [l, b]
                elif l == merged[a][0]:
                    merged[a].append(b)
        for a in A:
            dfs(a, a, set(A) - {a})
        return res[0]
        

if __name__ == "__main__":
    sl=Solution()
    A=["catg","ctaagt","gcta","ttca","atgcatc"]
    print(sl.shortestSuperstring(A))
```

## 思路

思路：

这道题在实现上还是有一定难度的，这里使用了dfs的思想。

首先创建一个merged字典，其中保存A的每个子串以及它对应的存在后面拼接覆盖最长的子串的覆盖长度以及子串。

itertools.combinations(A, 2)，这个方法依次遍历，A中的所有两个元素组合的情况。并通过merge函数，创建mergerd字典。

接下来就是关键的dfs方法了，它包括三个参数，当前的超级串，当前的子串(用于寻找下一个最长的子串)，剩余的子串集合。

使用时遍历所有的子串，即使所有的子串都放到第一个位置试一试，然后向后查找。

dfs方法中，先将当前的超级串与剩余子串集合中所有集合的长度相加，与最终结果res比较，如果小，则更新res。

下面就是寻找下一个子串，通过当前子串在merged字典中寻找下一个子串，如果有多个则遍历所有的。然后更新当前的超级串，当前的子串，以及剩余的子串集合。

如果寻找下一个子串是剩余的子串都没有覆盖的部分(merged字典中找不到)，就遍历剩下所有无覆盖子串nex，再找与nex有覆盖的子串，有的话更新dfs的参数，继续递归。

如果没有，前面刚开始的时候已经比较字符串的长度了。直接返回即可。