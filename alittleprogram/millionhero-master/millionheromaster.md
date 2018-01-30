# 百万英雄答题助手

---

> * 自定义百度搜索函数
> * 答题助手代码

---

## 自定义搜索函数

为了方便处理数据，自定义一个百度搜索函数。比较散，就不放代码了。就放在baiduSearch文件夹中。用的时候将它与下面答题助手的代码放在同一目录中即可。

主要思想：

输入：待搜索的关键字

输出：含多条格式化信息的集合

步骤，首先调用自定义的get函数，传入想要搜索的关键字，get返回搜索结果的页面，然后调用自定义的process函数，解析页面，返回每一条搜索的结果。

##代码

主要思想：

1. 获取截屏
2. 找到待检测问题位置，保存新图片
3. 使用baidu ocr进行文字识别
4. 百度搜索问题
5. 按顺序打印答案

```python
import sys
import base64
import json,os,time
import baiduSearch
import urllib.request
from PIL import Image
from aip import AipOcr
#获取开始时间
start = time.time()
#通过os.system在命令行输入指令
#输入 adb(android调试桥) 相关的命令，直接控制手机获取手机截屏，并保存在指定目录
#将指定目录下的图片传到电脑的当前目录
os.system("adb shell /system/bin/screencap -p /sdcard/screenshot.png") 
os.system("adb pull /sdcard/screenshot.png ./screenshot.png")

""" （百度ocr）你的 APPID AK SK """
#直接在百度ocr注册，获取免费的文字识别的服务
APP_ID = '10688198'
API_KEY = 'UL6273MpBvEvB8DPuNhkyzyp'
SECRET_KEY = '4RDGOAge9ZQnAZMXUUPXcddFUmNKnVuL'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
#打开图片
im = Image.open(r"./screenshot.png")   
#图片大小
img_size = im.size
w = im.size[0]
h = im.size[1]
print("xx:{}".format(img_size))

region = im.crop((70,200, w-70,700))    #裁剪的区域
#保存裁剪区域的图片
region.save(r"./crop_test1.png")

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
image = get_file_content(r"./crop_test1.png")
respon = client.basicGeneral(image)
titles = respon['words_result']          #获取问题
ans = ''
for title in titles:
      ans = ans +title['words']

print(ans)       #打印问题

keyword = ans    #识别的问题文本

convey = 'n'

if convey == 'y' or convey == 'Y':
    results = baiduSearch.search(keyword, convey=True)
elif convey == 'n' or convey == 'N' or not convey:
    results = baiduSearch.search(keyword)
else:
    print('输入错误')
    exit(0)
count = 0
for result in results:
    #print('{0} {1} {2} {3} {4}'.format(result.index, result.title, result.abstract, result.show_url, result.url))  # 此处应有格式化输出
	print('{0}'.format(result.abstract))  # 此处应有格式化输出
	count=count+1
	if(count == 2):      #这里限制了只显示2条结果，可以自己设置
		break

end = time.time()
print('程序用时：'+str(end-start)+'秒')
```

