#107_Binary_Tree_Level_Order_Traversal_II

------

> - 问题
> - 代码
> - 思路

## 问题

107.二叉树的层次遍历 II

给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

 

例如：

给定二叉树[3, 9, 20, null, null, 15, 7],

 

​    3

   / \

  9  20

​    /  \

   15   7

返回其自底向上的层次遍历为：

 

[

  [15,7],

  [9,20],

  [3]

]

## 代码

```python
import collections

class Solution:
    def levelOrderBottom(self, root):
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
        return res[::-1]
```

## 思路

思路：

与102题一样，之需将结果倒叙输出即可

 