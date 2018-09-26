#68_Text_Justification

---

> * 题目
> * 代码
> * 思路

---

##题目

68. 文本左右对齐

给定一个单词数组和一个长度 maxWidth，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。

你应该使用“贪心算法”来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。

要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。

文本的最后一行应为左对齐，且单词之间不插入额外的空格。

说明:

单词是指由非空格字符组成的字符序列。

每个单词的长度大于 0，小于等于 maxWidth。

输入单词数组 words 至少包含一个单词。

示例:

输入:

words = ["This", "is", "an", "example", "of", "text", "justification."]

maxWidth = 16

输出:

[

​    "This    is    an",

​    "example  of text",

​    "justification.  "

]

示例 2:

 

输入:

words = ["What", "must", "be", "acknowledgment", "shall", "be"]

maxWidth = 16

输出:

[

​    "What   must   be",

​    "acknowledgment  ",

​    "shall be        "

]

解释: 注意最后一行的格式应为 "shall be    " 而不是 "shall     be",

​    因为最后一行应为左对齐，而不是左右两端对齐。

​    第二行同样为左对齐，这是因为这行只包含一个单词。

示例 3:

输入:

words = ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain",

​        "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"]

maxWidth = 20

输出:

[

​    "Science  is  what we",

​    "understand      well",

​    "enough to explain to",

​    "a  computer.  Art is",

​    "everything  else  we",

​    "do                  "

]

## 代码

```python
class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        result=[]
        v=0
        while v < len(words):
            start=v
            # print("start",start)
            num=1
            sumlength=0
            # ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain",
            # "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"]
            while sumlength<=maxWidth and start+num-1<len(words):
                sumlength=0
                for j in range(num):
                    sumlength+=len(words[v+j])
                sumlength+=num-1
                # print("sumlength=",sumlength)
                if sumlength > maxWidth:
                    break
                num+=1
            num-=1
            sumlen=0
            for s in range(num):
                sumlen+=len(words[start+s])
            # print("num=",num)
            v=start+num
            if v<=len(words)-1:
                if num==1:
                    temp = words[start]+" "*(maxWidth - sumlen)
                    result.append(temp)
                elif (maxWidth - sumlen) % (num-1) == 0:
                    temp=""
                    for i in range(num):
                        if i!=num-1:
                            temp += words[start+i]+" "*((maxWidth - sumlen)//(num-1))
                        else:
                            temp += words[start+i]+" " * \
                                ((maxWidth - sumlen) -len(temp)-len(words[start+i]))
                    result.append(temp)
                else:
                    temp=""
                    for i in range(num):
                        if i < (maxWidth-sumlen) % (num-1):
                            temp += words[start+i]+" " * \
                                ((maxWidth - sumlen)//(num-1)+1)
                            
                        elif i==num-1:
                            temp += words[start+i]+" " * \
                                ((maxWidth - sumlen) - len(temp)-len(words[start+i]))
                        else:
                            temp += words[start+i]+" " * \
                                ((maxWidth - sumlen)//(num-1))
                    result.append(temp)
            else:
                temp=""
                while start<len(words):
                    temp+=words[start]+" "
                    start+=1
                left = maxWidth-len(temp)
                if left>=0:
                    temp+=" "*left
                else:
                    temp=temp[:left]
                result.append(temp)
        return result   

if __name__=="__main__":
    sl=Solution()
    result = sl.fullJustify(
        ["for", "your", "country"],
        16)
    for i in result:
        print(i)
```

## 思路

我们在处理的时候也要一行一行的来处理，首先要做的就是确定每一行能放下的单词数，这个不难，

就是比较n个单词的长度和加上n - 1个空格的长度跟给定的长度L来比较即可，找到了一行能放下的单词个数，

然后计算出这一行存在的空格的个数，是用给定的长度L减去这一行所有单词的长度和。得到了空格的个数之后，

就要在每个单词后面插入这些空格，这里有两种情况，比如某一行有两个单词"to" 和 "a"，给定长度L为6，

如果这行不是最后一行，那么应该输出"to   a"，如果是最后一行，则应该输出 "to a  "，

所以这里需要分情况讨论，最后一行的处理方法和其他行之间略有不同。最后一个难点就是，如果一行有三个单词，

这时候中间有两个空，如果空格数不是2的倍数，那么左边的空间里要比右边的空间里多加入一个空格，

那么我们只需要用总的空格数除以空间个数，能除尽最好，说明能平均分配，除不尽的话就多加个空格放在左

边的空间里，以此类推