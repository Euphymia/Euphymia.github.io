#129 Sum Root to Leaf Numbers

---

> * 问题
> * 代码
> * 思路

---

## 问题

Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

​    1

   / \

  2   3

The root-to-leaf path 1->2 represents the number 12.

The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.

## 代码

```c++
#include <bits/stdc++.h>
using namespace std;
// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};
int NodeID=0;
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
class Solution
{
  public:
    int sumNumbers(TreeNode *root){
        return sumNumbersDFS(root,0);
    }
    int sumNumbersDFS(TreeNode *root,int res){
        if(!root) return 0;
        res = res*10+root->val;
        if(!root->right&&!root->left) return res;
        return sumNumbersDFS(root->left,res)+sumNumbersDFS(root->right,res);
    }
};
int main(){
    Solution sl;
    char c[] = {0, 1, 2,0,0,3};
    int n = 5;
    TreeNode *root = CreateBiTree(c, n);
    cout<<sl.sumNumbers(root);
    getchar();
    return 0;
}
```

## 思路

利用DFS递归来解，这道题由于不是单纯的把各个节点的数字相加，而是每到一个新的数字，要把原来的数字扩大10倍之后再相加。