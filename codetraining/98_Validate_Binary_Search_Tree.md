#98 Validate Binary Search Tree

---

> * 问题
> * 代码
> * 具体思路
> * 树的使用方法

---

## 问题

给定一个二叉树，判断其是否是一个有效的二叉搜索树。

一个二叉搜索树有如下定义：

左子树只包含小于当前节点的数。

右子树只包含大于当前节点的数。 

所有子树自身必须也是二叉搜索树。

## 代码

```c++
#include <bits/stdc++.h>
using namespace std;
//  * Definition for a binary tree node.
struct TreeNode
{
    int val;    
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL){};
};
class Solution{
public:
    bool isValidBST(TreeNode *root){
        return isValidBST(root, LONG_MIN, LONG_MAX);
    }
    bool isValidBST(TreeNode *root,long min,long max){
        if(!root) return true;
        if(root->val<=min || root->val>=max) return false;
        return isValidBST(root->left,min,root->val)&&isValidBST(root->right,root->val,max);
    }
};
class Solution2
{
  public:
    bool isValidBST(TreeNode *root)
    {
        if (!root)
            return true;
        vector<int> vals;
        inorder(root, vals);
        for (int i = 0; i < vals.size() - 1; ++i)
        {
            if (vals[i] >= vals[i + 1])
                return false;
        }
        return true;
    }
    void inorder(TreeNode *root, vector<int> &vals)
    {
        if (!root)
            return;
        inorder(root->left, vals);
        vals.push_back(root->val);
        inorder(root->right, vals);
    }
};
int main(){
    Solution sl;
    Solution2 sl2;
    // 自己先建立一个二叉搜索树
    TreeNode *t1=new TreeNode(8);
    TreeNode *t=t1;
    int j=0;
    int nums[]={3,15,1,5,0,2};
    for(int i=0;i<3;i++){
        TreeNode *t2=new TreeNode(nums[j++]);
        t1->left=t2;
        TreeNode *t3=new TreeNode(nums[j++]);
        t1->right=t3;
        t1=t1->left;
    }
    cout<<sl.isValidBST(t);
    getchar();
    return 0;
}
```

## 具体思路

思路1：

利用其本身性质来做，初始化时带入系统最大值和最小值，在递归过程中换成它们自己的节点值，

用long代替int就是为了包括int的边界条件

思路2：

利用它本身的性质来做，即左 < 根 < 右，也可以通过利用中序遍历结果为有序数列来做。

## 树的使用方法

树的使用方法：

```c++
 定义树节点：
struct TreeNode
{
    int val;    
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL){};
};
 // 建立一个二叉搜索树
    TreeNode *t1=new TreeNode(8);
    TreeNode *t=t1;
    int j=0;
    int nums[]={3,15,1,5,0,2};
    for(int i=0;i<3;i++){
        TreeNode *t2=new TreeNode(nums[j++]);
        t1->left=t2;
        TreeNode *t3=new TreeNode(nums[j++]);
        t1->right=t3;
        t1=t1->left;
```

