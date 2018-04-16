#79 Word Search

---

> * 问题
> * 代码
> * 思路

---

## 问题

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell,

where "adjacent" cells are those horizontally or vertically neighboring. 

The same letter cell may not be used more than once.

For example,

Given board =

[

  ['A','B','C','E'],

  ['S','F','C','S'],

  ['A','D','E','E']

]

word = "ABCCED", -> returns true,

word = "SEE", -> returns true,

word = "ABCB", -> returns false.

##代码

```C++
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        if(word.empty()) return true;
        if(board.empty()||board[0].empty()) return false;
        vector<vector<bool>> visited(board.size(),vector<bool>(board[0].size(),false));
        for(int i=0;i<board.size();++i){
            for(int j=0;j<board[i].size();++j){
                if(search(board,word,0,i,j,visited)) return true;
            }
        } 
        return false;
    }
    bool search(vector<vector<char>> board,string word,int idx,int i,int j,vector<vector<bool>> visited){
        if(idx==word.size()) return true;
        if(i<0||j<0||i>=board.size()||j>=board[0].size()||visited[i][j]||board[i][j]!=word[idx]) 
            return false;
        visited[i][j]=true;
        bool res = search(board, word, idx + 1, i + 1, j, visited) ||
               search(board, word, idx + 1, i - 1, j, visited) ||
               search(board, word, idx + 1, i, j + 1, visited) ||
               search(board, word, idx + 1, i, j - 1, visited);
        visited[i][j] = false;
        return res;
    }
};
int main()
{
    Solution sl;
    vector<char> v1={'A','B','C','E'};
    vector<char> v2={'S','F','C','S'};
    vector<char> v3={'A','D','E','E'};
    vector<vector<char>> board={v1,v2,v3};
    cout<<sl.exist(board,"ABCCED")<<endl;
    cout<<sl.exist(board,"SEE")<<endl;
    cout<<sl.exist(board,"ABCB")<<endl;
    getchar();
    return 0;
}
```

## 思路

这道题是典型的深度优先遍历DFS的应用，原二维数组就像是一个迷宫，可以上下左右四个方向行走，我们以二维数组中每一个数都作为起点和给定字符串做匹配，我们还需要一个和原数组等大小的visited数组，是bool型的，用来记录当前位置是否已经被访问过，因为题目要求一个cell只能被访问一次。如果二维数组board的当前字符和目标字符串word对应的字符相等，则对其上下左右四个邻字符分别调用DFS的递归函数，只要有一个返回true，那么就表示可以找到对应的字符串，否则就不能找到