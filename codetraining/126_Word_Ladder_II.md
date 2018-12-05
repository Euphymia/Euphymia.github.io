#126_Word_Ladder_II

------

> - 问题
> - 代码
> - 思路

------

## 问题

 126.单词接龙 II

 

给定两个单词（beginWord 和 endWord）和一个字典 wordList，找出所有从 beginWord 到 endWord 的最短转换序列。转换需遵循如下规则：

 

每次转换只能改变一个字母。

转换过程中的中间单词必须是字典中的单词。

说明:

 

如果不存在这样的转换序列，返回一个空列表。

所有单词具有相同的长度。

所有单词只由小写字母组成。

字典中不存在重复的单词。

你可以假设 beginWord 和 endWord 是非空的，且二者不相同。

示例 1:

 

输入:

beginWord = "hit",

endWord = "cog",

wordList = ["hot","dot","dog","lot","log","cog"]

 

输出:

[

  ["hit","hot","dot","dog","cog"],

  ["hit","hot","lot","log","cog"]

]

示例 2:

 

输入:

beginWord = "hit"

endWord = "cog"

wordList = ["hot","dot","dog","lot","log"]

 

输出: []

 

解释: endWord "cog" 不在字典中，所以不存在符合要求的转换序列。

## 代码

```python
import copy
import collections 
class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        dic=collections.defaultdict(list)
        for i in wordList:
            for j in range(len(i)):
                temp=list(i)
                temp[j]='_'
                new_word="".join(temp)
                dic[new_word].append(i)
        wordset=set()
        wordset.add(beginWord)
        queue=collections.deque()
        queue.append([beginWord])
        res=[]
        flag=False
        while queue:    
            length=len(queue)
            for i in range(length):
                word=queue.popleft()
                for j in range(len(word[-1])):
                    temp=list(word[-1])
                    temp[j]="_"
                    new_word="".join(temp)
                    if word[-1]==endWord:
                        res.append(word)
                        flag=True
                        break
                    for w in dic[new_word]:
                        if w in wordset:
                            continue
                        else:
                            temp_word=copy.deepcopy(word)
                            temp_word.append(w)
                            queue.append(temp_word)
            for m in queue:
                if m[-1]!=endWord:
                    wordset.add(m[-1])
            if flag:
                return res
        return res


if __name__ == "__main__":
    sl=Solution()
    beginWord = "a"
    endWord = "c"
    wordList =["a","b","c"]
    print(sl.findLadders(beginWord,endWord,wordList))
```

## 思路

思路：

与127题很像，不过这次需要把单词改变的路径记录下来。所以res每次保存的都是一个路径数组，每次处理的都是数组的最后一个元素。

使用dfs，length记录每层处理的个数，flag记录是否结束循环。

wordset是为了防止单词过多循环，每次添加wordset的位置也是因为，放在这里可以避免同一层的单词冲突(同一层可以同时转换成一个单词)。

temp_word的深度拷贝是因为不深度拷贝的话加入到queue后，改变word，queue也会改变。所以每次重新创建一个temp_word。