# Learning of tensorflow(二)

---

> * 将tensorflow设置的变量保存到本地
> * 获取本地的tensorflow变量
> * 实现一个三层的神经网络并画出图像

---

##将tensorflow设置的变量保存到本地

```python
# Save to file
# remenmber to define the same dtype and same shape when restore
W=tf.Variable([[1,2,3],[1,2,3]],dtype=tf.float32,name='Weights')
b=tf.Variable(np.ones(3).reshape(1,3),dtype=tf.float32,name='Biases')

init=tf.initialize_all_variables()

saver=tf.train.Saver()
with tf.Session() as sess:
    sess.run(init)
    save_path=saver.save(sess,"my_net/save_net.ckpt")
    print("save to path",save_path)
```

##获取本地的tensorflow变量

注意在获取变量时，需要先定义好接受变量值的变量，其中shape，type都必须相同

```
# restore variables
# redefine the same dtype and same shape for your variase
W=tf.Variable(np.arange(6).reshape(2,3),dtype=tf.float32,name='Weights')
b=tf.Variable(np.ones((1,3)),dtype=tf.float32,name='Biases')

saver=tf.train.Saver()
with tf.Session() as sess1:
    # sess1.run(init)
    saver.restore(sess1,"my_net/save_net.ckpt")
    print("weight=",sess1.run(W))
    print("biases=",sess1.run(b))
```

## 实现一个三层的神经网络并画出图像

```python
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
# 定义添加神经层的函数
def add_layer(inputs,in_size,out_size,activation_funtion=None):
    Weights=tf.Variable(tf.random_normal([in_size,out_size]))
    biases=tf.Variable(tf.zeros([1,out_size])+0.1)
    Wx_plus_b=tf.matmul(inputs,Weights)+biases
    if activation_funtion is None:
        outputs=Wx_plus_b 
    else:
        outputs=activation_funtion(Wx_plus_b)
    return outputs

#create nn 1:10:1
#定义训练数据集
x_data = np.linspace(-1,1,300)[:,np.newaxis]
#添加点噪声，使数据浮动
noise = np.random.normal(loc=0,scale=0.05,size=x_data.shape)
y_data = np.square(x_data)-0.5+noise
#定义传入值
xs=tf.placeholder(tf.float32,[None,1])
ys=tf.placeholder(tf.float32,[None,1])
#定义第一层
l1 = add_layer(xs,1,10,activation_funtion=tf.nn.relu)
#输出层
prediction = add_layer(l1,10,1,activation_funtion=None)

loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys-prediction),reduction_indices=[1]))
#使用梯度下降算法最小化误差
train_step=tf.train.GradientDescentOptimizer(0.1).minimize(loss)

init=tf.initialize_all_variables()
#画出原始的训练数据
fig=plt.figure()
ax=fig.add_subplot(111)
ax.scatter(x_data,y_data)
#plt.ion() 表示连续plot
plt.ion()
plt.show()
with tf.Session() as sess:
    sess.run(init)
    for i in range(1000):
        sess.run(train_step,feed_dict={xs:x_data,ys:y_data})
        if i%50==0:
            try:
                #删除已有的一条线
                ax.lines.remove(lines[0])
            except Exception:
                pass
            # print(sess.run(loss,feed_dict={xs:x_data,ys:y_data}))
            #得到预测值
            prediction_value=sess.run(prediction,feed_dict={xs:x_data})
            #将ax画出的线存进lines中
            lines=ax.plot(x_data,prediction_value)
            #表示plot暂停0.1秒
            plt.pause(0.1)
```

