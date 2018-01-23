# Notes of matplotlib

---

> * 简单画图
> * 将window分为多份用来画图
> * 在同一张图中画图
> * 连续画图
> * 暂停显示画图
> * 画出3D的图像

---

## 代码

```python
import matplotlib.pyplot as plt
import numpy as np

#define the data
x=np.linspace(0,6,100)[:,np.newaxis]
siny=np.sin(x)
cosy=np.cos(x)

#draw two picture in two window
fig = plt.figure()
ax=fig.add_subplot(1,2,1)
ax.scatter(x,siny,color='r')
ax.scatter(x,cosy,color='g')
bx=fig.add_subplot(1,2,2)
bx.scatter(x,siny,color='r')
bx.scatter(x,cosy,color='g')
plt.show()
plt.pause(1)

#draw two picture in one window 
#散点图  加‘or’
plt.plot(x,siny,'or')
plt.plot(x,cosy,'or',color='g')
plt.show()
plt.pause(1)
#直线图 default
plt.plot(x,siny)
plt.plot(x,cosy,color='g')
plt.show()
```

## 画出3D的图像

这里需要引入mpl_toolkits.mplot3d中的Axes3D函数完成3D画图

## 代码

```python
import matplotlib.pyplot as plt  
from mpl_toolkits.mplot3d import Axes3D  
ax = plt.figure().add_subplot(111, projection = '3d')  
#基于ax变量绘制三维图  
#xs表示x方向的变量  
#ys表示y方向的变量  
#zs表示z方向的变量，这三个方向上的变量都可以用list的形式表示  
#m表示点的形式，o是圆形的点，^是三角形（marker)  
#c表示颜色（color for short）  
xs=[0,0,1,1]
ys=[0,1,0,1]
zs=[0,1,1,0]
xs1=[0,0,1,1]
ys1=[0,1,0,1]
zs1=[1,0,0,1]
ax.scatter(xs,ys,zs, c='b', marker = '^') #点为红色三角形  
ax.scatter(xs1,ys1,zs1,c='r',marker='*')
#设置坐标轴  
ax.set_xlabel('X Label')  
ax.set_ylabel('Y Label')  
ax.set_zlabel('Z Label')  
  
#显示图像  
plt.show()  
```

