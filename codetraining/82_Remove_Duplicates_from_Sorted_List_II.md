# 82_Remove_Duplicates_from_Sorted_List_II

---

> * 问题
> * 代码
> * 思路

---

## 问题

\82. 删除排序链表中的重复元素 II

给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。

 

示例 1:

 

输入: 1->2->3->3->4->4->5

输出: 1->2->5

示例 2:

 

输入: 1->1->1->2->3

输出: 2->3

## 代码

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # T(n) = O(n)
        dummy = ListNode(0)
        dummy.next = head
        p, q = dummy, dummy.next
        while p and q:
            found_duplicate = False
            while q.next and q.next.val == q.val:
                found_duplicate = True
                p.next = q.next
                q = q.next
            if found_duplicate:
                p.next = q.next
            else:
                p = p.next
            q = q.next
        return dummy.next
if __name__=="__main__":
    testlist=[1,1,2,4,5]
    p=ListNode(0)
    head=p
    for i in testlist:
        p.next=ListNode(i)
        p=p.next
    sl=Solution()
    result=sl.deleteDuplicates(head.next)
    while result!=None:
        print(result.val,end="")
        result=result.next
```



##思路

思路：

先初始化p,q的位置，p是指向头结点的指针，q是头结点，然后开始循环

found_duplicate标记，表示是否出现连续值。

如果q与q下一个节点的值相同，则将q一直循环到不同为止，此时标记为真，p则指向q的下一个位置(跳过重复节点)

如果q与q下一个节点的值不同，将p指向p的下一个节点(将p延伸，保存值不同的节点)