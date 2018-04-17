# 02 Binary Tree Traverse With Recursion

---

> * 使用递归处理二叉树的遍历问题
> * 代码

---

```c++
// 使用递归的方法，解决三种二叉树遍历的问题。先序，中序，后序。
#include <iostream>
using namespace std;

struct BiNode
{
    char data;
    BiNode *lchild, *rchild;
};
BiNode *BiTree;

int NodeID;
// 自动创建二叉树，二叉树长度为n，当NodeID大于n时结束。
// 当遇到'0'字符时，返回空指针，所以可以用'0'，控制数的形状，否则数一直沿左子树增长。
BiNode *CreateBiTree(char c[], int n)
{
    BiNode *T;
    NodeID++;
    if (NodeID > n)
    {
        return (NULL);
    }
    if (c[NodeID] == '0')
    {
        return (NULL);
    }
    T = new BiNode;
    T->data = c[NodeID];
    T->lchild = CreateBiTree(c, n);
    T->rchild = CreateBiTree(c, n);
    return (T);
}
// 先序
void PreOrderTraverse(BiNode *T)
{
    if (T)
    {
        cout << T->data << " ";
        PreOrderTraverse(T->lchild);
        PreOrderTraverse(T->rchild);
    }
}
// z中序
void InOrderTraverse(BiNode *T)
{
    if (T)
    {
        InOrderTraverse(T->lchild);
        cout << T->data << " ";
        InOrderTraverse(T->rchild);
    }
}
// 后序
void PostOrderTraverse(BiNode *T)
{
    if (T)
    {
        PostOrderTraverse(T->lchild);
        PostOrderTraverse(T->rchild);
        cout << T->data << " ";
    }
}

int main()
{
    int i, SampleNum=10;
    char c[100]={'v','a','b','d','0','0','e','0','0','c','f'};
    // cin >> SampleNum;
    // for (i = 1; i <= SampleNum; i++)
    // {
    //     cin >> c[i];
    // }
    NodeID = 0;
    BiTree = CreateBiTree(c, SampleNum);
    PreOrderTraverse(BiTree);
    cout << endl;
    InOrderTraverse(BiTree);
    cout << endl;
    PostOrderTraverse(BiTree);
    getchar();
    return 0;
}
```

