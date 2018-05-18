# 04 Find Min Max

---

> * 问题
> * 代码
> * 思路
> * format的使用方法

---

## 问题

在一个有一千个数的数组里，找出里面的最大值和最小值。

## 代码

```python
import numpy as np
def findMaxMin(nums):
    min=nums[0]
    max=nums[0]
    for i in nums:
        if i>max:
            max=i
        elif i<min:
            min =i
    return max,min
def test():
    nums=np.random.randint(1000,size=1000)
    max,min=findMaxMin(nums)
    print("max=",max,"\nmin=",min)
    for i in range(len(nums)//100):
        print("{} {}".format(i,nums[i]))
    print('{:,}'.format(100000000))
if __name__=='__main__':
    test()
```

##思路

在循环体中使用 if elif比使用两个if要快

## format的使用方法

```python
python中format函数用于字符串的格式化
通过关键字
1 print('{名字}今天{动作}'.format(名字='陈某某', 动作='拍视频'))  # 通过关键字
2 grade = {'name': '陈某某', 'fenshu': '59'}
3 print('{name}电工考了{fenshu}'.format(**grade))  # 通过关键字，可用字典当关键字传入值时，在字典前加**即可
通过位置
1 print('{1}今天{0}'.format('拍视频', '陈某某'))  # 通过位置
2 print('{0}今天{1}'.format('陈某某', '拍视频'))
填充和对齐 ^ < > 分别表示居中、左对齐、右对齐，后面带宽度
1 print('{:^14}'.format('陈某某'))
2 print('{:>14}'.format('陈某某'))
3 print('{:<14}'.format('陈某某'))
4 print('{:*<14}'.format('陈某某'))
5 print('{:&>14}'.format('陈某某'))  # 填充和对齐^<>分别表示居中、左对齐、右对齐，后面带宽度
精度和类型f精度常和f一起使用
1 print('{:.1f}'.format(4.234324525254))
2 print('{:.4f}'.format(4.1))
进制转化，b o d x 分别表示二、八、十、十六进制
print('{:b}'.format(250))
print('{:o}'.format(250))
print('{:d}'.format(250))
print('{:x}'.format(250))
千分位分隔符，这种情况只针对与数字
print('{:,}'.format(100000000))
print('{:,}'.format(235445.234235))
```

