# Draw a picture of heart

使用turtle包中的函数画一个心形o.o

```python
from turtle import *
#定义函数 边前进边右转前进200个像素
def curvemove():
    for i in range(200):
        right(1)
        forward(1)
#设置线的颜色以及图像的颜色
color('red','pink') 
#开始 
begin_fill()
#选择一个角度
left(140)
#前进111.65个像素
forward(111.65)
#调用定义的curvemove函数
curvemove()
#左转120°
left(120)
#继续画弧
curvemove()
#前进
forward(111.65)
#结束
end_fill()
done()
```

![drawheart](drawheart.PNG)