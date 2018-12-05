#125 Valid Palindrome

---

> * 问题
> * 代码
> * 具体思路

---

## 问题

给定一个字符串，确定它是否是回文，只考虑字母数字字符和忽略大小写。

例如：

"A man, a plan, a canal: Panama" 是回文字符串。 "race a car" 不是回文字符串。

注意 : 你有考虑过这个字符串可能是空的吗？ 在面试中这是一个很好的问题。

针对此题目，我们将空字符串定义为有效的回文字符串。

## 代码

```c++
#include <bits/stdc++.h>
using namespace std;
class Solution
{
  public:
    bool isPalindrome(string s)
    {
        int left=0,right=s.size()-1;
        while(left<right){
            if(!isValid(s[left])) left++;
            else if(!isValid(s[right])) right--;
            else if((s[left]+32-'a')%32!=(s[right]+32-'a')%32) return false;
            else {
                left++;
                right--;
            }
        }
        return true;
    }
    bool isValid(char ch){
        if(ch>='0' && ch<='9') return true;
        if(ch>='a' && ch<='z') return true;
        if(ch>='A' && ch<='Z') return true;
        return false;
    }
};
int main(){
    Solution sl;
    string s = "A man, a plan, a canal: Panama";
    cout<<sl.isPalindrome(s);
    getchar();
    return 0;
}
```

```python
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        temp_s=[]
        for i in s[::-1]:
            if i.isdigit():
                temp_s.append(i)
            elif i.isalpha():
                temp_s.append(i.lower())
        return temp_s==temp_s[::-1]

if __name__ == "__main__":
    sl=Solution()
    s="A man, a plan, a canal: Panama"
    print(sl.isPalindrome(s))
```



## 具体思路

思路：

验证回文字符串是比较常见的问题，所谓回文，就是一个正读和反读都一样的字符串，比如“level”或者“noon”等等就是回文串。但是这里，加入了空格和非字母数字的字符，增加了些难度，但其实原理还是很简单：只需要建立两个指针，left和right, 分别从字符的开头和结尾处开始遍历整个字符串，如果遇到非字母数字的字符就跳过，继续往下找，直到找到下一个字母数字或者结束遍历，如果遇到大写字母，就将其转为小写。等左右指针都找到字母数字时，比较这两个字符，若相等，则继续比较下面两个分别找到的字母数字，若不相等，直接返回false.

时间复杂度为O(n)

python

很简单，首先处理s字符串，只保留数字和字母，并将字母变为小写。

返回转换后的数组的正序，倒序等价结果即可