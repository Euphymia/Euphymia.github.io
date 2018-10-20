#103_Binary_Tree_Zigzag_Level_Order_Traversal

------

> - 问题
> - 代码
> - 思路

## 问题

103.二叉树的锯齿形层次遍历

给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

 

例如：

给定二叉树[3, 9, 20, null, null, 15, 7],

 

​    3

   / \

  9  20

​    /  \

   15   7

返回锯齿形层次遍历如下：

 

[

  [3],

  [20,9],

  [15,7]

]

## 代码

```python
import collections
class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        Q = collections.deque([root])
        res = []
        level = 1
        while Q:
            rec = [] # record all node in the same level
            l = len(Q)
            for i in range(l):
                node = Q.popleft()
                rec.append(node.val)
                if node.left: Q.append(node.left)
                if node.right: Q.append(node.right)
            # 循环结束rec正好储存了该层的所有节点
            if level % 2 != 0: res.append(rec)
            else: res.append(rec[::-1])
            level += 1
        return res
```

## 思路

思路：

与102类似，，无非是在处理某些层时，记录的节点顺序需要反转一下，引入一个level变量判定是否反转即可