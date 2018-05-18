# 拷贝u盘中的文件到电脑

---

> * 程序介绍
> * shutil模块
> * 运行介绍
> * python 与 pythonw

---

## 程序介绍

首先，这是一个可以在后台运行的一个copy插入u盘中所有文件的程序。

程序通过不断的扫描是否有新的硬盘插入，这里为了在自己电脑上实现方便，只检测的是否有G：盘的出现，为了增加程序的健壮性，可以添加H：盘等其他盘的检测，因实际电脑的硬盘划分而改变。

扫描到新硬盘(G)，即u盘的出现时，将u盘中所有的数据通过shutil模块中的copytree将u盘中的所有文件都拷贝到目标目录(这里拷贝的E盘的copy文件夹中)

但是，为了不盲目的拷贝，我们不使用copytree方法(全部拷贝)，而是使用shutil的copy2方法只拷贝所需文件。文件的选取是通过判断文件的大小来实现的，首先遍历u盘中的所有文件，获取它们的大小，小于期初设定的大小(程序中设为50M)，即可拷贝到电脑的目标目录下。为了分开不同的u盘，程序以每次u盘插入的时间不同，将u盘中的文件拷贝的不同的以时间命名的文件夹中。

##shutil模块

```python
import shutil

#先清空name.db，然后把chen.txt的内容写入name.db里
#shutil.copyfileobj(open("chen.txt","r"),open("name.db","w"))

#将文件chen.txt的全部拷贝到name.db
#shutil.copyfile("chen.txt","name.db")

#将chen.txt文件的权限拷贝给name.db，其他的不变
#shutil.copymode("chen.txt","name.db")

#仅拷贝状态的信息，包括：mode bits, atime, mtime, flags
#shutil.copystat("chen.txt","name.db")

#拷贝chen.txt这个文本的内容和权限到name.db这个文本
#shutil.copy("chen.txt","name.db")

#拷贝chen.txt这个文件的内容和状态到name.db
#shutil.copy2("chen.txt","name.db")

#递归地把me这个文件夹的内容复制到file2里面，ignore表示的是排除了哪些内容
#shutil.copytree("me","fil2",ignore=shutil.ignore_patterns('*.py','temp*'))

#递归删除一个文件夹
#shutil.rmtree("fil2")

#mv移动文件，相当于重新
#shutil.move("me","file2")

#将root_dir指定的目录下的文件进行压缩
#shutil.make_archive("G:/123/wwwww","gztar",root_dir="G:/123/ZIP file")
```

## 运行介绍

为了使程序能再后台运行，将文件类型改为了pyw。

运行时在dos命令行使用pythonw

输入 pythonw usb_autocopy.pyw 即可

然后插入u盘进行测试，关闭dos窗口也不影响，可以在任务管理器中关闭python.exe进行关闭。

##pythonw与python

```
严格来说，它们之间的不同就只有一个：视窗运行它们的时候调用不同的执行档案。

视窗用 python.exe 运行 .py ，用 pythonw.exe 运行 .pyw 。
这纯粹是因为安装视窗版 Python 时，扩展名 .py 自动被登记为用 python.exe 运行的文件，
而 .pyw 则被登记为用 pythonw.exe 运行。

.py 和 .pyw 之间的“其它差别”全都是 python.exe 和 pythonw.exe 之间的差别。

跟 python.exe 比较起来，pythonw.exe 有以下的不同：
1）执行时不会弹出控制台窗口（也叫 DOS 窗口）
2）所有向原有的 stdout 和 stderr 的输出都无效
3）所有从原有的 stdin 的读取都只会得到 EOF

.pyw 格式是被设计来运行开发完成的纯图形界面程序的。
纯图形界面程序的用户不需要看到控制台窗口。

值得一提的是，开发纯图形界面程序的时候，你可以暂时把 .pyw 改成 .py ，
以便运行时能调出控制台窗口，看到所有错误信息，方便除虫。

注：唯独视窗版 Python 有 .pyw 格式。
```