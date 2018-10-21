# 911_Online_Election

------

> - 问题
> - 代码
> - 思路

------

## 问题

 911.在线选举

在选举中，第 i 张票是在时间为 times[i] 时投给 persons[i] 的。

现在，我们想要实现下面的查询函数： TopVotedCandidate.q(int t) 将返回在 t 时刻主导选举的候选人的编号。

在 t 时刻投出的选票也将被计入我们的查询之中。在平局的情况下，最近获得投票的候选人将会获胜。

示例：

输入：["TopVotedCandidate", "q", "q", "q", "q", "q", "q"], [[[0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]], [3], [12], [25], [15], [24], [8]]

输出：[null, 0, 1, 1, 0, 0, 1]

解释：

时间为 3，票数分布情况是[0]，编号为 0 的候选人领先。

时间为 12，票数分布情况是[0, 1, 1]，编号为 1 的候选人领先。

时间为 25，票数分布情况是[0, 1, 1, 0, 0, 1]，编号为 1 的候选人领先（因为最近的投票结果是平局）。

在时间 15、24 和 8 处继续执行 3 个查询。

提示：

1 <= persons.length = times.length <= 5000

0 <= persons[i] <= persons.length

times 是严格递增的数组，所有元素都在[0, 10 ^ 9] 范围中。

每个测试用例最多调用 10000 次 TopVotedCandidate.q。

TopVotedCandidate.q(int t) 被调用时总是满足 t >= times[0]。

## 代码

```python
class MyTopVotedCandidate:
    
    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        self.vote_set={}
        person_list=[0 for i in range(max(persons)-min(persons)+1)]
        for person,time in zip(persons,times):
            person_list[person]+=1
            persom_max=max(person_list)
            idxs = [idx for idx, e in enumerate(person_list) if e ==persom_max]
            if len(idxs)==1:
                temp=idxs[0]
            elif len(idxs)==len(person_list):
                temp=person
            else:
                position=times.index(time)
                for pos in range(position,-1,-1):
                    if persons[pos] in idxs:
                        temp=persons[pos]
                        break
            self.vote_set[time]=temp

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """  
        time_list=list(self.vote_set.keys())
        time_list.sort()
        for i in range(len(time_list)):
            if t<time_list[i]:
                return self.vote_set[time_list[i-1]]
        return self.vote_set[time_list[-1]]

import bisect
class TopVotedCandidate:

    def __init__(self, persons, times):
        self.leads, self.times, count = [], times, {}
        lead = -1
        for t, p in zip(times, persons):
            count[p] = count.get(p, 0) + 1
            if count[p] >= count.get(lead, 0):
                lead = p
            self.leads.append(lead)

    def q(self, t):
        return self.leads[bisect.bisect(self.times, t) - 1]
if __name__=="__main__":
    sl = TopVotedCandidate([0, 0, 1, 1, 2], [0, 67, 69, 74, 87])
    Q = [[4], [62],[100], [88], [70], [73], [22], [75], [29], [10]]
    for i in Q:
        print(sl.q(i[0]))
```

## 思路

思路：

先解释一下输入，"TopVotedCandidate"对应一个二维数组[[0, 1, 1, 0, 0, 1, 0],[0, 5, 10, 15, 20, 25, 30]]，前一个数组表示投票给0或者1，后一个数组表示在什么时刻投的票。

接下来的"q"就是查询了，对应的[3], [12], [25], [15], [24], [8]表示在这六个时刻分别进行查询。

首先介绍我的方法MyTopVotedCandidate

初始化时保存一个字典，键为每个时间点，值为每个时间点对应的选举人。查询时按照时刻，返回字典中刚刚大于t时刻的键值前一个时刻的值。

 

别人的方法TopVotedCandidate

通过共享times不需要保存一个字典，之需按顺序保存对应时刻的选举人列表即可。

使用字典get方法，查询该字典是否存在需要的键，没有则返回第二个默认值。

在q()查询函数中，使用了bisect二分查找方法，返回插入的位置，-1即可得对应位置的数值。