# Notes of matplotlib

---

> * 简单画图
> * 将window分为多份用来画图
> * 在同一张图中画图
> * 连续画图
> * 暂停显示画图

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

