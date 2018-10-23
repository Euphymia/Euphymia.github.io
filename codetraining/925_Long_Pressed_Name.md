#925_Long_Pressed_Name

------

> - 问题
> - 代码
> - 思路

------

## 问题

 925.长按键入

你的朋友正在使用键盘输入他的名字 name。偶尔，在键入字符 c 时，按键可能会被长按，而字符可能被输入 1 次或多次。

 

你将会检查键盘输入的字符 typed。如果它对应的可能是你的朋友的名字（其中一些字符可能被长按），那么就返回 True。

 

 

示例 1：

 

输入：name = "alex", typed = "aaleex"

输出：true

解释：'alex' 中的 'a' 和 'e' 被长按。

示例 2：

 

输入：name = "saeed", typed = "ssaaedd"

输出：false

解释：'e' 一定需要被键入两次，但在 typed 的输出中不是这样。

示例 3：

 

输入：name = "leelee", typed = "lleeelee"

输出：true

示例 4：

 

输入：name = "laiden", typed = "laiden"

输出：true

解释：长按名字中的字符并不是必要的。

 

 

提示：

 

name.length <= 1000

typed.length <= 1000

name 和 typed 的字符都是小写字母。

## 代码

```python
class Solution:
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        i=j=0
        if name[-1]!=typed[-1]:
            return False
        while j<len(typed):
            if name[i]==typed[j]:
                i=i+1 if i<len(name)-1 else i
                j+=1
            elif typed[j] == typed[j-1]:
                j+=1
            else: return False
        return True

if __name__=="__main__":
    sl = Solution()
    name = "alex"
    typed = "aaleex"
    print(sl.isLongPressedName(name,typed))
```

## 思路

 思路：

很简单，首先如果两个字符串最后一个字符不相同，肯定返回false，否则

开始比较两个字符串，如果相等，i，j同时+1, 这时还要保证i不会超出name的范围，否则，若typed[j] == typed[j-1]。j+1，否则返回false。

如果遍历到最后，返回true

 