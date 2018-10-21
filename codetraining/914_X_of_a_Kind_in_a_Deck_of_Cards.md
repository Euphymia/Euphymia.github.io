# 914_X_of_a_Kind_in_a_Deck_of_Cards

------

> - 问题
> - 代码
> - 思路

---

## 问题

 914.卡牌分组

给定一副牌，每张牌上都写着一个整数。

 

此时，你需要选定一个数字 X，使我们可以将整副牌按下述规则分成 1 组或更多组：

 

每组都有 X 张牌。

组内所有的牌上都写着相同的整数。

仅当你可选的 X >= 2 时返回 true。

 

 

示例 1：

 

输入：[1, 2, 3, 4, 4, 3, 2, 1]

输出：true

解释：可行的分组是[1, 1]，[2, 2]，[3, 3]，[4, 4]

示例 2：

 

输入：[1, 1, 1, 2, 2, 2, 3, 3]

输出：false

解释：没有满足要求的分组。

示例 3：

 

输入：[1]

输出：false

解释：没有满足要求的分组。

示例 4：

 

输入：[1, 1]

输出：true

解释：可行的分组是[1, 1]

示例 5：

 

输入：[1, 1, 2, 2, 2, 2]

输出：true

解释：可行的分组是[1, 1]，[2, 2]，[2, 2]

 

提示：

 

1 <= deck.length <= 10000

0 <= deck[i] < 10000

## 代码

```python
class Solution:
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        set_deck=set(deck)
        if len(set_deck)==len(deck):
            return False
        count_dic = dict().fromkeys(list(set_deck), 0)
        for i in deck:
            count_dic[i]+=1
        values=count_dic.values()
        min_value=min(values)
        for i in range(2,min_value+1):
            flag=True
            for j in values:
                if j%i==0:
                    continue
                else:
                    flag=False
                    break
            if flag:
                return True
        return False


if __name__=="__main__":
    sl=Solution()
    input_deck = [1, 1, 1, 2, 2, 2, 3, 3]
    input_deck2 = [1, 2, 3, 4, 4, 3, 2, 1]
    input_deck3 = [1, 1, 1, 2, 2, 2, 3, 3]
    print(sl.hasGroupsSizeX(input_deck3))

```

## 思路

思路：

​    记录每个数字出现的次数，再找出他们的最大公约数，如果存在，切大于1小于最小的数字个数，则为true