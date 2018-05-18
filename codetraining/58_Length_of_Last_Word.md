#58 Length of Last Word

---

> * 问题
> * 代码
> * 思路

---

## 问题

最后一个单词的长度

给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。

如果不存在最后一个单词，请返回 0 。

说明：一个单词是指由字母组成，但不包含任何空格的字符串。

示例:

输入: "Hello World"

输出: 5

## 代码

```python
class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        i=len(s)-1
        while i>=0 and s[i]==" ":
            i-=1
        slist=s[0:i+1].split(" ")
        return len(slist[len(slist)-1])

def test():
    sl=Solution()
    print(sl.lengthOfLastWord(" world    "))


if __name__=='__main__':
    test()
```

