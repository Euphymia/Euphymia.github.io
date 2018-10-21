# 127 Word Ladder

---

> * 问题
> * 代码
> * 具体思路

---

## 问题

单词接龙

给出两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的最短转换序列，转换需遵循如下规则：

每次只能改变一个字母。 变换过程中的中间单词必须在字典中出现。 例如，给出：

beginWord = "hit" endWord = "cog" wordList = [ "hot", "dot", "dog", "lot", "log", "cog" ]

一个最短的变换序列是： "hit"->"hot"->"dot"->"dog"->"cog"， 返回长度 5。

注意 :

如果没有这样的转换序列，则返回0。 所有单词具有相同的长度。 所有单词只包含小写字母字符。 您可能会认为单词列表中没有重复项。

 你可能会认为 beginWord 和 endWord 是非空的并且不一样。

## 代码

```c++
#include <bits/stdc++.h>
using namespace std;
class Solution
{
  public:
    int ladderLength(string beginWord, string endWord, vector<string> &wordList)
    {
        unordered_set<string> dict(wordList.begin(),wordList.end());
        queue<string> que;
        que.push(beginWord);
        que.push("");
        int res=1;
        while(!que.empty()){
            string str=que.front();
            que.pop();
            if(str!=""){
                int len=str.length();
                for(int i=0;i<len;i++){
                    char temp=str[i];
                    for(char ch='a';ch<='z';ch++){
                        if(ch==temp) continue;
                        str[i]=ch;
                        if(dict.count(str)&&str==endWord) {
                            return res+1;
                        }
                        else if(dict.find(str)!=dict.end()){
                            que.push(str);
                            dict.erase(str);
                        }
                    }
                    str[i]=temp;
                }
            }
            else if(!que.empty()){
                res++;
                que.push("");
            }
        }
        return 0;
    }
};
int main()
{
    Solution sl;
    string beginword="hit",endword="cog";
    vector<string> wordlist = {"hot", "dot", "dog", "lot", "cog"};
    cout<<sl.ladderLength(beginword,endword,wordlist);
    getchar();
    return 0;
}
```

```python
#python
import collections
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        dic=collections.defaultdict(list)
        # dic={}
        for i in wordList:
            for j in range(len(i)):
                temp=list(i)
                temp[j]='_'
                a="".join(temp)
                dic[a].append(i)
        wordset=[beginWord]
        que=collections.deque()
        que.append(beginWord)
        res=1
        while que:
            l=len(que)
            for i in range(l):
                s=que.popleft()
                for j in range(len(s)):
                    temp = list(s)
                    temp[j] = '_'
                    a = "".join(temp)
                    if s==endWord:
                        return res
                    if a in dic.keys():
                        for m in dic[a]:
                            if m in wordset:
                                continue
                            else:
                                que.append(m)
                                wordset.append(m)
            res+=1
        return 0

if __name__=="__main__":
    sl=Solution()
    print(sl.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))

```

## 具体思路

思路：

分析：这种题，肯定是每次改变单词的一个字母，然后逐渐搜索，很多人一开始就想到用dfs，其实像这种求最短路径、树最小深度问题bfs最适合。

本题bfs要注意的问题：

和当前单词相邻的单词是：对当前单词改变一个字母且在字典中存在的单词找到一个单词的相邻单词，加入bfs队列后，要从字典中删除，因为不删除的话会造成类似于hog->hot->hog的死循环。而删除对求最短路径没有影响，因为我们第一次找到该单词肯定是最短路径，即使后面其他单词也可能转化得到它，路径肯定不会比当前的路径短

bfs队列中用NULL来标识层与层的间隔，每次碰到层的结尾，遍历深度 +1 我们利用和求二叉树最小深度层序遍历的方法来进行bfs