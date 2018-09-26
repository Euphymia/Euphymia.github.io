# 76_Minimum_Window_Substring

---

> * 问题
> * 代码
> * 思路

---

## 问题

\76. 最小覆盖子串

给定一个字符串 S 和一个字符串 T，请在 S 中找出包含 T 所有字母的最小子串。

示例：

输入: S = "ADOBECODEBANC", T = "ABC"

输出: "BANC"

说明：

如果 S 中不存这样的子串，则返回空字符串 ""。

如果 S 中存在这样的子串，我们保证它是唯一的答案。	

## 代码

```python
import copy
import collections
class Solution:
    def minWindow(self,s,t):
        if len(s)<len(t):
            return ""
        res=""
        left = 0
        right = 0
        count = 0
        minLen = len(s)+1
        tdict=collections.Counter(t)
        while right<len(s):
            if s[right] in tdict.keys():
                tdict[s[right]]-=1
                if tdict[s[right]]>=0:
                    count+=1
                while count==len(t):
                    if right-left+1<minLen:
                        minLen=right-left+1
                        res=s[left:right+1]
                    if s[left] in tdict.keys():
                        tdict[s[left]]+=1
                        if tdict[s[left]]>0:
                            count-=1
                    left+=1
            right+=1
        return res
    def minWindow2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # 此方法极慢，垃圾
        if len(s)<len(t):
            return ""
        tdict = collections.Counter(t)
        resultleft=0
        resultright=0
        minsum=len(s)
        m=len(s)-1
        while s[m] not in tdict.keys() and m>=0:
            m-=1
        s=s[0:m+1]
        for left in range(len(s)):
            tempdict=copy.deepcopy(tdict)
            # tempdict = collections.Counter(t)
            if s[left] not in tempdict.keys():
                continue
            right=left+len(t)
            if right>len(s):
                break
            for i in s[left:right]:
                if i in tempdict.keys():
                    if tempdict[i]>0:
                        tempdict[i]-=1
            while sum(tempdict.values())>0 and right<len(s):
                tempdict[s[right]]-=tempdict[s[right]]>0
                # if s[right] in tempdict.keys():
                #     if tempdict[s[right]]>0:
                #             tempdict[s[right]]-=1
                right+=1
            if sum(tempdict.values())==0 and right-left<=minsum:
                resultleft=left
                resultright=right
                minsum=right-left
        return s[resultleft:resultright]

                    
if __name__=="__main__":
    sl=Solution()
    result=sl.minWindow("ADOBECODEBANC","ABC")
    print(result)
```



##思路

思路：

这道题的要求是要在O(n)的时间度里实现找到这个最小窗口字串，那么暴力搜索Brute Force肯定是不能用的，我们可以考虑哈希表，其中key是T中的字符，value是该字符出现的次数。

 

\- 我们最开始先扫描一遍T，把对应的字符及其出现的次数存到哈希表中。

 

\- 然后开始遍历S，遇到T中的字符，就把对应的哈希表中的value减一，直到包含了T中的所有的字符，纪录一个字串并更新最小字串值。

 

\- 将子窗口的左边界向右移，略掉不在T中的字符，如果某个在T中的字符出现的次数大于哈希表中的value，则也可以跳过该字符。