#19 Remove Nth Node From End of List

---

> * 问题
> * 代码
> * 思路

---

##问题

删除链表的倒数第N个节点

给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.

说明：

给定的 n 保证是有效的。

## 代码

```c++
#include<bits/stdc++.h>
using namespace std;
// Definition for singly-linked list.
struct ListNode {
  int val;
  ListNode *next;
  ListNode(int x) : val(x), next(NULL) {}
};
class Solution{
  public:
    ListNode *removeNthFromEnd(ListNode *head, int n){
      ListNode realHead(0);
      realHead.next = head;
      head = &realHead;
      ListNode *curr = &realHead;
      while (n-- > 0)
        curr = curr->next;
      while (curr->next != nullptr)
      {
        curr = curr->next;
        head = head->next;
      }

      head->next = head->next->next;
      return realHead.next;
    }
};
int main(){
  Solution sl;
  ListNode *p1=new ListNode(1);
  ListNode *p=p1;
  for(int i=2;i<=5;i++){
    p1->next=new ListNode(i);
    p1=p1->next;
  }
  ListNode *p0=sl.removeNthFromEnd(p,5);
  while(p0!=NULL){
    cout<<p0->val<<",";
    p0=p0->next;
  }
  getchar();
  return 0;
}
```

## 思路

先获取倒数第k个ListNode节点的指针，令头指针q1向后移k个节点，再令一个新头指针q2与指向第k个节点的指针同时向后移动，直到q1指到末尾，此时q2指向倒数第k个指针。令q2指向第二个节点即可。