#904_Fruit_Into_Baskets

------

> - 问题
> - 代码
> - 思路

## 问题

904.水果成篮

 

在一排树中，第 i 棵树产生 tree[i] 型的水果。

你可以从你选择的任何树开始，然后重复执行以下步骤：

 

把这棵树上的水果放进你的篮子里。如果你做不到，就停下来。

移动到当前树右侧的下一棵树。如果右边没有树，就停下来。

请注意，在选择一颗树后，你没有任何选择：你必须执行步骤 1，然后执行步骤 2，然后返回步骤 1，然后执行步骤 2，依此类推，直至停止。

 

你有两个篮子，每个篮子可以携带任何数量的水果，但你希望每个篮子只携带一种类型的水果。

用这个程序你能收集的水果总量是多少？

 

 

示例 1：

 

输入：[1, 2, 1]

输出：3

解释：我们可以收集[1, 2, 1]。

示例 2：

 

输入：[0, 1, 2, 2]

输出：3

解释：我们可以收集[1, 2, 2].

如果我们从第一棵树开始，我们将只能收集到[0, 1]。

示例 3：

 

输入：[1, 2, 3, 2, 2]

输出：4

解释：我们可以收集[2, 3, 2, 2].

如果我们从第一棵树开始，我们将只能收集到[1, 2]。

示例 4：

 

输入：[3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]

输出：5

解释：我们可以收集[1, 2, 1, 1, 2].

如果我们从第一棵树或第八棵树开始，我们将只能收集到 4 个水果。

 

 

提示：

 

1 <= tree.length <= 40000

0 <= tree[i] < tree.length

每一样数字代表一种水果，你只能连续取两种水果，每次取一个，看看最多取多少

 

## 代码

```python
class Solution:
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        treelength=len(tree)
        result=1
        start=0
        i=0
        while i<treelength:
            flag=[tree[i]]
            if treelength-i-1<result:
                break
            j=i+1
            res=1
            while j<treelength:
                if tree[j] not in flag and len(flag)<2:
                    flag.append(tree[j])
                    start=j
                    res+=1
                elif tree[j] in flag:
                    res+=1
                else:
                    break
                j+=1
            i=start if i<start else i+1 
            result=result if result>res else res
        return result
if __name__=="__main__":
    sl=Solution()
    a = [0, 1, 1]
    print(sl.totalFruit(a))
```

## 思路

思路：

注意 0也是一种水果。思路很清晰，不过要想加快速度，除了判断每次i开始到最后的长度与result的值的大小，一提前结束循环

还可以在循环时记录第一次出现第二种水果的位置，作为下次开始的位置，start