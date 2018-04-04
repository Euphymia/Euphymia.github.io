# 73 Set Matrix Zeroes

---

> * 问题
> * 代码
> * 主要思路

---

## 问题

问题：矩阵赋零

给定一个 m x n 的矩阵，如果一个元素为 0 ，则将这个元素所在的行和列都置零。

你有没有使用额外的空间? 使用 O(mn) 的空间不是一个好的解决方案。 

使用 O(m + n) 的空间有所改善，但仍不是最好的解决方案。 

你能设计一个使用恒定空间的解决方案吗？

## 代码

```c++
#include <bits/stdc++.h>
using namespace std;
class Solution
{
  public:
    void setZeroes(vector<vector<int>> &matrix)
    {
        int row=matrix.size();
        int col=matrix[0].size();
        // row0，col0分别记录第一行，第一列是否存在0
        int col0=-1,row0=-1;
        // 判断第一行是否存在0，若存在将row0置零
        for (int j = 0; j < col; j++)
        {
            if (matrix[0][j] == 0)
            {
                row0 = 0;
            }
        }
        for(int i=0;i<row;i++){
            // 判断第一列是否存在0，若存在将col置零
            if(matrix[i][0]==0) col0=0;
            for(int j=1;j<col;j++){
                // 将矩阵中除第一行第一列以外，凡是0的元素对应的第一行，第一列的元素置零
                // 用于记录准备置零的位置
                if(matrix[i][j]==0){
                    matrix[0][j]=0;
                    matrix[i][0]=0;
                }
            }
        }
        // 将除了matrix[0][0]元素之外的，第一行，第一列为零的元素对应的行和列置零
        for(int i=1;i<row;i++){
            if(matrix[i][0]==0){
                for(int k=0;k<col;k++){
                    matrix[i][k]=0;
                }
            }
        }
        for(int j=1;j<col;j++){
            if(matrix[0][j]==0){
                for(int k=0;k<row;k++){
                    matrix[k][j]=0;
                }
            }
        }
        // 若row0为零，将第一行置零
        if(row0==0){
            for(int k=0;k<col;k++){
                matrix[0][k]=0;
            }
        }
        // 若col0为零，将第一列置零
        if(col0==0){
            for(int k=0;k<row;k++){
                matrix[k][0]=0;
            }
        }
    }
};
int main(){
    Solution sl;
    vector<vector<int>> m(5,vector<int>(5));
    int num=1;
    for(int i=0;i<5;i++){
        for(int j=0;j<5;j++){
            m[i][j]=num;
            num++;
        }
    }
    m[1][1]=0;
    m[2][3]=0;
    sl.setZeroes(m);
    for(int i=0;i<5;i++){
        for(int j=0;j<5;j++){
            cout<<m[i][j]<<" ";
        }
        cout<<endl;
    }
    getchar();
    return 0;
}
```

## 主要思路

思路：

这道题中说的空间复杂度为O(mn)的解法自不用多说，直接新建一个和matrix等大小的矩阵，然后一行一行的扫，只要有0，就将新建的矩阵的对应行全赋0，行扫完再扫列，然后把更新完的矩阵赋给matrix即可，这个算法的空间复杂度太高。将其优化到O(m + n) 的方法是，用一个长度为m的一维数组记录各行中是否有0，用一个长度为n的一维数组记录各列中是否有0，最后直接更新matrix数组即可。

这道题的要求是用O(1) 的空间，那么我们就不能新建数组，我们考虑就用原数组的第一行第一列来记录各行各列是否有0.具体步骤在代码中。