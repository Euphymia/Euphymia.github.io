# 基于q-learning的Flippybird游戏

---

> * 代码简要介绍
> * 核心思想
> * 代码本目录下

---

## 代码简要介绍

文件中包括如下几个文件，

1. asset文件夹，用于存放pygame运行时必须的图片和音频。
2. qvalues.json，已经训练好的q表
3. initialize_qvalues.py，初始化(全变0)q表
4. bot.py，基于q-learning的机器学习对象
5. flappy.py，flappybird游戏(已加入bot)

运行时，先进入当前目录，运行flappy.py即可。

## 核心思想

代码内部附有详细注释，这里交代一下核心思想。

1. **flappybird的实现**

这里的flappybird基于pygame实现，其实就是根据用户的输入，不断刷新游戏页面，已达游戏效果。pygame中坐标的零点是在坐上角。

值得注意的是调整一些参数，比如地面图片刷新幅度的设定，已达到跟管道同时向左移动的效果。

这里的管道也是通过一张图实现的，上面的管道即使下面的管道旋转180°得到的。

getHitmask函数，获取图片像素所在位置，在检查小鸟是否与管道相撞时有用

在运行时，不断检查小鸟有没有发生碰撞，碰撞则游戏结束，没有则更新画面，管道左移，地面左移，重新获取小鸟的坐标，开启音效，改变小鸟动作等等

2. bot.py的实现

bot定义的一个自己飞的小鸟机器人的类。在flappybird.py中，游戏开始时创建机器人，根据小鸟的处于的不同状态(距离管道相对的位置xdif，ydif以及小鸟当时在y方向上的速度)，通过查看q表(qvalues.json)中的数据，产生相应的动作，飞或不飞。小鸟发生碰撞后，根据小鸟之前飞行的状态以及相应动作，更新q表，惩罚最近的两个动作，奖励之前的动作。

## 代码本目录下

