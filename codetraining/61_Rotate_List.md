#61_Rotate_List.py

---

> * 问题
> * 代码
> * 思路

---

## 问题

\61. 旋转链表

给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: 1->2->3->4->5->NULL, k = 2

输出: 4->5->1->2->3->NULL

解释:

向右旋转 1 步: 5->1->2->3->4->NULL

向右旋转 2 步: 4->5->1->2->3->NULL

示例 2:

输入: 0->1->2->NULL, k = 4

输出: 2->0->1->NULL

解释:

向右旋转 1 步: 2->0->1->NULL

向右旋转 2 步: 1->2->0->NULL

向右旋转 3 步: 0->1->2->NULL

向右旋转 4 步: 2->0->1->NULL

## 代码

```python
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        t1 = t2 = head
        l = 1
        if head == None or head.next == None:
            return head
        while t1.next != None:
            l += 1
            t1 = t1.next
        if k >= l:
            len_to_travel = l - k % l
        else:
            len_to_travel = l - k

        if len_to_travel == 0:
            return head
        else:
            while len_to_travel > 1:
                t2 = t2.next
                len_to_travel -= 1
            t1.next = head
            head = t2.next
            t2.next = None

        return head

if __name__=='__main__':
    ln=ListNode(1)
    head=ln
    for i in range(5):
        ln.next=ListNode(i+2)
        ln=ln.next
    sl=Solution()
    res=sl.rotateRight(head,2)
    for i in range(6):
        print(res.val)
        res=res.next
```

## 思路

思路：

我刚开始拿到这题首先想到的就是用快慢指针来解，快指针先走k步，然后两个指针一起走，当快指针走到末尾时，

慢指针的下一个位置是新的顺序的头结点，这样就可以旋转链表了，自信满满的写完程序，放到OJ上跑，以为能一次通过，

结果跪在了各种特殊情况，首先一个就是当原链表为空时，直接返回NULL，还有就是当k大于链表长度和k远远大于链表长度时该如何处理，

我们需要首先遍历一遍原链表得到链表长度n，然后k对n取余，这样k肯定小于n，就可以用上面的算法了，