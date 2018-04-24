#11 Container With Most Water

---

> * 问题
> * 代码
> * 思路

---

## 问题

盛最多水的容器

给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。画 n 条垂直线，使得垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。

找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

注意：你不能倾斜容器，n 至少是2。

## 代码

```c++
#include <bits/stdc++.h>
using namespace std;
// Solution1使用递归的方法，但是时间复杂度不过关
class Solution1
{
  public:
    int maxArea(vector<int> &height)
    {
        int maxCon = 0;
        findMaxCon(0, height, maxCon);
        return maxCon;
    }
    void findMaxCon(int left, vector<int> &height, int &maxCon)
    {
        if (left == height.size() - 1)
            return;
        for (int i = left + 1; i < height.size(); ++i)
        {
            int con = min(height[left], height[i]) * (i - left);
            maxCon = con > maxCon ? con : maxCon;
        }
        findMaxCon(left + 1, height, maxCon);
    }
};
//solution2，时间复杂度为O(n)
int maxArea(vector<int> &height)
{
    int water = 0;
    int i = 0, j = height.size() - 1;
    while (i < j)
    {
        int h = min(height[i], height[j]);
        water = max(water, (j - i) * h);
        while (height[i] <= h && i < j)
            i++;
        while (height[j] <= h && i < j)
            j--;
    }
    return water;
}
int main()
{
    Solution sl;
    vector<int> v = {1, 2, 3, 4};
    cout << sl.maxArea(v);
    getchar();
    return 0;
}
```

## 思路

Start by evaluating the widest container, using the first and the last line.All other possible containers are less wide, so to hold more water, they need to be higher.Thus, after evaluating that widest container, skip lines at both ends that don't support a higher height.Then evaluate that new container we arrived at. Repeat until there are no more possible containers left.