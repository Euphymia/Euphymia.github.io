# 83_Remove_Duplicates_from_Sorted_List

---

> * 问题
> * 代码
> * 思路

---

## 问题

\83. 删除排序链表中的重复元素

给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

 

示例 1:

 

输入: 1->1->2

输出: 1->2

示例 2:

 

输入: 1->1->2->3->3

输出: 1->2->3

Definition for singly-linked list.

class ListNode:

​    def __init__(self, x):

​        self.val = x

​        self.next = None

 

## 代码

```python

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        p, q = dummy, dummy.next
        while p and q:
            found_duplicate = False
            while q.next and q.next.val == q.val:
                found_duplicate = True
                p.next = q.next
                q = q.next
            p = p.next
            q = q.next
        return dummy.next

```



##思路

思路：

此题与82题很像只是少了判断是否存在重复元素，并以此决定是否留下第一个元素