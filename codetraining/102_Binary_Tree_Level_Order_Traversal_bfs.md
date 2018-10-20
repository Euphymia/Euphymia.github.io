#102_Binary_Tree_Level_Order_Traversal

------

> - 问题
> - 代码
> - 思路

## 问题

102.二叉树的层次遍历

给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

例如:

给定二叉树: [3, 9, 20, null, null, 15, 7],

​    3

   / \

  9  20

​    /  \

   15   7

返回其层次遍历结果：

 

[

  [3],

  [9,20],

  [15,7]

]

## 代码

```python
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

思路：

首先输入是[3, 9, 20, null, null, 15, 7],

使用广度优先输出结果