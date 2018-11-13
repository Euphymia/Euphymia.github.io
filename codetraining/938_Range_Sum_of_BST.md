#938_Range_Sum_of_BST

------

> - 问题
> - 代码
> - 思路

------

## 问题

 938.二叉搜索树的范围和

给定二叉搜索树的根结点 root，返回 L 和 R（含）之间的所有结点的值的和。

二叉搜索树保证具有唯一的值。

示例 1：

输入：root = [10,5,15,3,7,null,18], L = 7, R = 15

输出：32

示例 2：

输入：root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10

输出：23

提示：

树中的结点数量最多为 10000 个。

最终的答案保证小于 2^31。

## 代码

```python
Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        res = 0
        if root == None:
            return 0
        
        if root.val >= L and root.val <= R:
            res += root.val
        
        res += self.rangeSumBST(root.left, L, R)
        res += self.rangeSumBST(root.right, L, R)
        return res
```

## 思路

思路

对于二叉树的题目，一般还是从递归入手。可以让当前节点的值和L、R比较，根据情况再递归的进入子节点。