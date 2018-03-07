# 答题卡识别

---

> * 识别步骤
> * 代码

---

## 识别步骤

### 实现答题卡识别的7步

- **Step #1:** 检测到图片中的答题卡
- **Step #2:** 应用透视变换来提取图中的答题卡（以自上向下的鸟瞰视图）
- **Step #3:** 从透视变换后的答题卡中提取 the set of 气泡/圆点 (答案选项)
- **Step #4:** 将题目/气泡排序成行
- **Step #5:** 判断每行中被标记/涂的答案
- **Step #6:** 在我们的答案字典中查找正确的答案来判断答题是否正确
- **Step #7:** 为其它题目重复上述操作

## 代码

附带照片，测试时修改照片路径即可

```python
# 引入必要的库
from imutils.perspective import four_point_transform
from imutils import contours
import numpy as np
import argparse
import imutils
import cv2
 
# 构建答案字典，键为题目号，值为正确答案
ANSWER_KEY = {0: 1, 1: 4, 2: 0, 3: 3, 4: 1}

# 加载图片，将它转换为灰阶，轻度模糊，然后边缘检测。
image = cv2.imread("C:\\Users\\think\\Desktop\\666.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(blurred, 75, 200)

# 从边缘图中寻找轮廓，然后初始化答题卡对应的轮廓
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]
docCnt = None
 
# 确保至少有一个轮廓被找到
if len(cnts) > 0:
    # 将轮廓按大小降序排序
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
 
    # 对排序后的轮廓循环处理
    for c in cnts:
        # 获取近似的轮廓
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
 
        # 如果我们的近似轮廓有四个顶点，那么就认为找到了答题卡
        if len(approx) == 4:
            docCnt = approx
            break
# 对原始图像和灰度图都进行四点透视变换
paper = four_point_transform(image, docCnt.reshape(4, 2))
warped = four_point_transform(gray, docCnt.reshape(4, 2))
# 对灰度图应用大津二值化算法
thresh = cv2.threshold(warped, 0, 255,
    cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    # 在二值图像中查找轮廓，然后初始化题目对应的轮廓列表
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]
questionCnts = []
 
# 对每一个轮廓进行循环处理
for c in cnts:
    # 计算轮廓的边界框，然后利用边界框数据计算宽高比
    (x, y, w, h) = cv2.boundingRect(c)
    ar = w / float(h)
 
    # 为了辨别一个轮廓是一个气泡，要求它的边界框不能太小，在这里边至少是20个像素，而且它的宽高比要近似于1
    if w >= 20 and h >= 20 and ar >= 0.9 and ar <= 1.1:
        questionCnts.append(c)
# 以从顶部到底部的方法将我们的气泡轮廓进行排序，然后初始化正确答案数的变量。
questionCnts = contours.sort_contours(questionCnts,
    method="top-to-bottom")[0]
correct = 0
 
# 每个题目有5个选项，所以5个气泡一组循环处理
for (q, i) in enumerate(np.arange(0, len(questionCnts), 5)):
    # 从左到右为当前题目的气泡轮廓排序，然后初始化被涂画的气泡变量
    cnts = contours.sort_contours(questionCnts[i:i + 5])[0]
    bubbled = None

# 对一行从左到右排列好的气泡轮廓进行遍历
    for (j, c) in enumerate(cnts):
        # 构造只有当前气泡轮廓区域的掩模图像
        mask = np.zeros(thresh.shape, dtype="uint8")
        cv2.drawContours(mask, [c], -1, 255, -1)
 
        # 对二值图像应用掩模图像，然后就可以计算气泡区域内的非零像素点。
        mask = cv2.bitwise_and(thresh, thresh, mask=mask)
        total = cv2.countNonZero(mask)
 
        # 如果像素点数最大，就连同气泡选项序号一起记录下来
        if bubbled is None or total > bubbled[0]:
            bubbled = (total, j)

# 初始化轮廓颜色为红色，获取正确答案序号
    color = (0, 0, 255)
    k = ANSWER_KEY[q]
 
    # 检查由填充气泡获得的答案是否正确，正确则将轮廓颜色设置为绿色。
    if k == bubbled[1]:
        color = (0, 255, 0)
        correct += 1
 
    # 画出正确答案的轮廓线。
    cv2.drawContours(paper, [cnts[k]], -1, color, 3)

# 计算分数并打分
score = (correct / 5.0) * 100
print("[INFO] score: {:.2f}%".format(score))
cv2.putText(paper, "{:.2f}%".format(score), (10, 30),
    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
cv2.imshow("Original", image)
cv2.imshow("Exam", paper)
cv2.waitKey(0)

```

