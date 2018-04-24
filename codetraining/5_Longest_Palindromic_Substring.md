#5 Longest Palindromic Substring

---

> * 问题
> * 代码
> * 思路

---

##问题

最长回文子串问题：给定一个字符串，求它的最长回文子串长度。

## 代码

```C++
#include <iostream>
#include <string>
#include <string.h>
using namespace std;

class Solution
{
  public:
    string longestPalindrome(string str)
    {
        // 数组p保存字符串str每个位置的最大回文串长度
        string strs = "$#";
        for (int i = 0; i < str.size(); i++)
        {
            strs += str[i];
            strs += "#";
        }
        str = strs;
        int *p = new int[str.size() + 1];
        memset(p, 0, sizeof(p));
        // mx表示当前扫描的回文串最右边的位置，id表示最右边为mx的回文串的中心
        int mx = 0, id = 0;
        for (int i = 1; i <= str.size(); i++)
        {
            if (mx > i)
            {
                // 如果 mx>i ，即当前扫描到的位置在mx的左边。
                // 然后分两种情况，
                // 1，i对应的id对称位置j的回文串长度小于i到mx的长度，
                // 则i位置周围必然存在与j相同长度的回文串，可以在此基础上继续向外判断知否是回文串。
                // 2，i到mx的长度小，则直接从mx的位置向外判断是否为回文串。
                // p[i]从i对应的id对称位置和i到mx的距离中选择一个小的开始向外判断回文串
                p[i] = min(p[2 * id - i], (mx - i));
            }
            else
            {
                // 如果mx<i，将p[1]从1开始
                p[i] = 1;
            }

            while (str[i - p[i]] == str[i + p[i]])
                p[i]++;
            // 更新mx和id
            if (i + p[i] > mx)
            {
                mx = i + p[i];
                id = i;
            }
        }
        // 从p中找出最大的数并记录它对应的位置
        int max = 0, ii;
        for (int i = 1; i < str.size(); i++)
        {
            if (p[i] > max)
            {
                ii = i;
                max = p[i];
            }
        }
        // max-1表示最大的回文串长度
        max--;
        // 输出最大的回文串
        int start = ii - max;
        int end = ii + max;
        string res = "";
        for (int i = start; i <= end; i++)
        {
            if (str[i] != '#')
            {
                res += str[i];
            }
        }
        return res;
    }
};

int main()
{
    Solution sl;
    string str = "aasdffdsa";
    cout << sl.longestPalindrome(str);
    getchar();
    return 0;
}
```

## 思路

使用manacher算法。