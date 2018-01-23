#使用tensorflow处理分类问题

---

> * 使用tensorflow处理分类问题
> * 代价函数交叉熵
> * 代码(直接运行)

---

## tensorflow处理分类问题

这里处理的数据集是mnist中的数据，先定义每层的函数(输入数据，输入维数，输出维数，激活函数)，包括每层包括的权重和偏执量，在定义计算准确率的函数

## 代价函数交叉熵

交叉熵常常与softmax配合用于处理多分类问题。

定义：![交叉熵函数](交叉熵函数.PNG)

## 代码(直接运行)

```python
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
#读取数据包，如果没有将直接下载，维度为28*28=784,类别分为10类
mnist = input_data.read_data_sets('MNIST_data',one_hot=True)

def add_layer(inputs,in_size,out_size,activation_funtion=None):
    #权重
    Weights = tf.Variable(tf.random_normal([in_size,out_size]))
    #偏执量，先初始化为0.1
    biases = tf.Variable(tf.zeros([1,out_size])+0.1) 
    #计算运算结果
    Wx_plus_b = tf.matmul(inputs,Weights)+biases
    #输入至激活函数(没有则直接输出)
    if activation_funtion is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_funtion(Wx_plus_b)
    return outputs
#计算训练好的神经网络的准确率
def compute_accuracy(v_xs,v_ys):
    #获取全局变量 prediction
    global prediction
    #定义测试集的测试结果为y_pre
    y_pre = sess.run(prediction,feed_dict={xs:v_xs})
    #定义正确的结果是比较测试结果和真实值
    correct_prediction = tf.equal(tf.argmax(y_pre,1),tf.argmax(v_ys,1))
    #定义正确率
    accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))

    #查看correct_predictiond的输出
    print(sess.run(correct_prediction,feed_dict={xs:v_xs,ys:v_ys}))
    # [ True  True  True ...,  True  True  True]

    #开始计算准确率
    result = sess.run(accuracy,feed_dict={xs:v_xs,ys:v_ys})

    return result
#define placeholder for inputs to network
xs = tf.placeholder(dtype=tf.float32,shape=[None,784]) #28*28
ys = tf.placeholder(dtype=tf.float32,shape=[None,10])

#add out put layer
prediction = add_layer(xs,784,10,activation_funtion=tf.nn.softmax)

#the error between prediction and real data
#这里使用交叉熵作为分类的损失函数
#常常将激活函数softmax + 损失函数交叉熵 用于分类问题
cross_entroy = tf.reduce_mean(-tf.reduce_sum(ys*tf.log(prediction),reduction_indices=[1]))
#定义最优化函数 GradientDescentOptimizei(梯度下降算法),优化cross_entroy，使之最小
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entroy)

sess = tf.Session()
sess.run(tf.initialize_all_variables())
#训练1000次
for i in range(1000):
    #重点：
    #这里每次使用训练集中的100个元素进行训练，大大减小了训练的时间，训练效果也可能更好。
    batch_x,batch_y = mnist.train.next_batch(100)
    #开启训练
    sess.run(train_step,feed_dict={xs:batch_x,ys:batch_y})
    if(i%50==0):
        #mnist.test.images 中有10000张图片数据,shape=[10000,784]
        print(compute_accuracy(mnist.test.images,mnist.test.labels))

```

