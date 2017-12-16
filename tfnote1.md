# Notes of tendorflow(一)

---

> * 定义tensorflow 的变量
> * run tensorflow  的两张方法
> * tensorflow的矩阵乘法
> * 利用placeholder在运行时传入值
> * 实现一个超级简单的一层网络(感知器)

---

```python
import tensorflow as tf
import numpy as np
#tensorflow 变量
state=tf.Variable(0,name='counter')
one=tf.constant(1)

new_value=tf.add(state,one)
update=tf.assign(state,new_value)

init=tf.initialize_all_variables()
#run tensorflow的两种方法
with tf.Session() as sess2:
    sess2.run(init)
    for _ in range(3):
        counter=sess2.run(update)
        print(counter)

#tensorflow的矩阵乘法
matrix1=tf.constant([[3,3]])
matrix2=tf.constant([[2],[2]])

product=tf.matmul(matrix1,matrix2)

sess1=tf.Session()
result=sess1.run(product)
print(result)

#利用placeholder 在运行的过程中传入值
input1=tf.placeholder(tf.float32)
input2=tf.placeholder(tf.float32)

output=tf.add(input1,input2)
init=tf.initialize_all_variables()
with tf.Session() as sess3:
    print(sess3.run(output,feed_dict={input1:[7.],input2:[3.]}))

#超级简单的训练一个一层的网络
#create data
x_data=np.random.rand(100).astype(np.float32)
y_data=x_data*0.1+0.3
#create tensorflow structure start
Weights=tf.Variable(tf.random_uniform([1],-1.0,1.0))
Biases=tf.Variable(tf.zeros(1))

y=Weights*x_data+Biases

loss=tf.reduce_mean(tf.square(y-y_data))
optimizer=tf.train.GradientDescentOptimizer(0.5)

train=optimizer.minimize(loss)

init = tf.initialize_all_variables()
#create tensorflow structure end
sess=tf.Session()
sess.run(init) #类似于一个指针

for step in range(201):
    sess.run(train)
    if step%20==0:
        print(step,sess.run(Weights),sess.run(Biases))
```

