#102_Binary Tree Level Order Traversal

---

> * 问题
> * 代码
> * 思路
> * 队列的使用方法

---

## 问题

二叉树层序遍历

给定一个二叉树，返回它的节点值的层序遍历（即从左到右，一层一层的）。

For example:

Given binary tree [3,9,20,null,null,15,7],

​    3

   / \

  9  20

​    /  \

   15   7

return its level order traversal as:

[

  [3],

  [9,20],

  [15,7]

]

## 代码

```c++
#include<bits/stdc++.h>
using namespace std;
// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};
int NodeID = 0;
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> res;
        if(root==NULL) return res;
        queue<TreeNode*> q;
        q.push(root);
        while(!q.empty()){
            vector<int> oneLevel;
            int size=q.size();
            for(int i=0;i<size;++i){
                TreeNode *node=q.front();
                q.pop();
                oneLevel.push_back(node->val);
                if(node->right) q.push(node->right);
                if(node->left) q.push(node->left);
            }
            res.push_back(oneLevel);
        }
        return res;
    }
};
TreeNode *CreateBiTree(char c[], int n)
{
    TreeNode *T;
    NodeID++;
    if (NodeID > n)
    {
        return (NULL);
    }
    if (c[NodeID] == 0)
    {
        return (NULL);
    }
    T = new TreeNode(1);
    T->val = c[NodeID];
    T->right = CreateBiTree(c, n);
    T->left = CreateBiTree(c, n);
    return (T);
}
int main()
{
    Solution sl;
    char c[]={0,1,2,0,0,3,4,0,0,5};
    int n=9;
    TreeNode *root=CreateBiTree(c,n);
    auto res=sl.levelOrder(root);
    for(int i=0;i<res.size();++i){
        for(int j=0;j<res[i].size();++j){
            cout<<res[i][j]<<",";
        }
        cout<<endl;
    }
    getchar();
    return 0;
}
```

```python
#python
import collections

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        Q = collections.deque([root])
        res = []
        while Q:
            rec = []  # record all node in the same level
            l = len(Q)
            for i in range(l):
                node = Q.popleft()
                rec.append(node.val)
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
            # 循环结束rec正好储存了该层的所有节点
            res.append(rec)
        return res
```



## 思路

层序遍历二叉树是典型的广度优先搜索BFS的应用，但是这里稍微复杂一点的是，我们要把各个层的数分开，存到一个二维向量里面，大体思路还是基本相同的，建立一个queue，然后先把根节点放进去，这时候找根节点的左右两个子节点，这时候去掉根节点，此时queue里的元素就是下一层的所有节点，用一个for循环遍历它们，然后存到一个一维向量里，遍历完之后再把这个一维向量存到二维向量里，以此类推，可以完成层序遍历。

## 队列的使用方法

queue 的基本操作举例如下：

queue入队，如例：q.push(x); 将x 接到队列的末端。

queue出队，如例：q.pop(); 弹出队列的第一个元素，注意，并不会返回被弹出元素的值。

访问queue队首元素，如例：q.front()，即最早被压入队列的元素。

访问queue队尾元素，如例：q.back()，即最后被压入队列的元素。

判断queue队列空，如例：q.empty()，当队列空时，返回true。

访问队列中的元素个数，如例：q.size()