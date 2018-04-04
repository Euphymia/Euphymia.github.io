## 88 Merge Sorted Array

---

> * 问题
> * 代码
> * 主要思路

---

## 问题

问题：

给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1中，使得 num1 成为一个有序数组。

注意 :

你可以假设 nums1有足够的空间（空间大小大于或等于m +n）来保存 nums2 中的元素。

在 nums1 和 nums2 中初始化的元素的数量分别是 m 和 n。

## 代码

```c++
#include <bits/stdc++.h>
using namespace std;
class Solution
{
  public:
    void merge(vector<int> &nums1, int m, vector<int> &nums2, int n)
    {
        if(n==0){
            return;
        }
        int length=m+n-1;
        int index=m+n-1;
        m--;
        n--;
        for(int i=0;i<length&n>=0&m>=0;i++){
            if(nums1[m]>=nums2[n]){
                nums1[index--]=nums1[m--];
            }
            else{
                nums1[index--]=nums2[n--];
            }
        }
        if(m<0){
            for(int i=0;i<=n;i++){
                nums1[i]=nums2[i];
            }
        }
    }
};
int main(){
    Solution sl;
    int n1[]={1,1,3,5,7,8,10,0,0,0,0};
    int n2[]={1,3,6,7};
    vector<int> num1(n1,n1+11);
    vector<int> num2(n2,n2+4);
    sl.merge(num1,7,num2,4);
    for(int i=0;i<num1.size();i++){
        cout<<num1[i]<<" ";
    }
    getchar();
    return 0;
}
```

## 主要思路

算法思想是：由于合并后A数组的大小必定是m+n，所以从最后面开始往前赋值，先比较A和B中最后一个元素的大小，把较大的那个插入到m+n-1的位置上，再依次向前推。如果A中所有的元素都比B小，那么前m个还是A原来的内容，没有改变。如果A中的数组比B大的，当A循环完了，B中还有元素没加入A，直接用个循环把B中所有的元素覆盖到A剩下的位置。