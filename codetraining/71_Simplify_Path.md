## 71_Simplify_Path

---

> * 问题
> * 代码
> * 思路

---

## 问题

\71. 简化路径

给定一个文档 (Unix-style) 的完全路径，请进行路径简化。

例如，

path = "/home/", => "/home"

path = "/a/./b/../../c/", => "/c"

边界情况:

你是否考虑了 路径 = "/../" 的情况？

在这种情况下，你需返回 "/" 。

此外，路径中也可能包含多个斜杠 '/' ，如 "/home//foo/" 。

在这种情况下，你可忽略多余的斜杠，返回 "/home/foo" 。

 

 ## 代码

```python
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        path2 = []
        for x in path.split('/'):
            if not x == '':
                path2.append(x)
        for x in path2:
            if x == '.':
                continue
            elif x == '..':
                if len(stack) == 0:
                    continue
                else:
                    stack.pop()
            else:
                stack.append(x)
        return '/' + '/'.join(stack)
if __name__=="__main__":
    sl=Solution()
    result=sl.simplifyPath("/...")
    print(result)

```

## 思路

思路：

这道题让简化给定的路径，光根据题目中给的那一个例子还真不太好总结出规律，应该再加上两个例子 path = "/a/./b/../c/", = > "/a/c"

和path = "/a/./b/c/", = > "/a/b/c"， 这样我们就可以知道中间是"."的情况直接去掉，是".."时删掉它上面挨着的一个路径，

而下面的边界条件给的一些情况中可以得知，如果是空的话返回"/"，如果有多个"/"只保留一个。那么我们可以把路径看做是由一个或多个"/"分割开的众多子字符串，

把它们分别提取出来一一处理即可