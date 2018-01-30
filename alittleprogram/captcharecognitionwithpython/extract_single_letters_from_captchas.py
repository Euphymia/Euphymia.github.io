#功能：抽取出验证码中的每一位数字并保存图片(为训练分类器做准备)
import os
import os.path
import cv2
import glob
import imutils
#captcha 验证码
#自我生成的验证码图片的名字
CAPTCHA_IMAGE_FOLDER = "generated_captcha_images"
#抽取出来的字幕图片名字
OUTPUT_FOLDER = "extracted_letter_images"

# Get a list of all the captcha images we need to process
#使用glob函数获取所需文件路径
captcha_image_files = glob.glob(os.path.join(CAPTCHA_IMAGE_FOLDER, "*"))
counts = {}

# loop over the image paths
#使用enumerate函数获取所有图片的枚举
#如[(0,image1),(1,image2),(2,image3).....]
for (i, captcha_image_file) in enumerate(captcha_image_files):
    print("[INFO] processing image {}/{}".format(i + 1, len(captcha_image_files)))
    # 输出样例>>>  [INFO] processing image 59/842   
    # Since the filename contains the captcha text (i.e. "2A2X.png" has the text "2A2X"),
    # 获取文件名
    filename = os.path.basename(captcha_image_file)
    #切分验证码名字，例如将'2A2X.png'切分成['2A2X','png']
    #这里获取前面的名字
    captcha_correct_text = os.path.splitext(filename)[0]

    #加载一张图片，将其转换成灰度图
    image = cv2.imread(captcha_image_file)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #在图片周围，添加一些小框
    # Add some extra padding around the image
    gray = cv2.copyMakeBorder(gray, 8, 8, 8, 8, cv2.BORDER_REPLICATE)
    # 转化成二值图，纯黑和纯白
    # threshold the image (convert it to pure black and white)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    # 找到图像的轮廓（连续的像素点）
    # cv2.findContours()函数首先返回一个list，list中每个元素都是图像中的一个轮廓，用numpy中的ndarray表示。
    # find the contours (continuous blobs of pixels) the image
    contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # 与不同的opencv版本兼容
    # Hack for compatibility with different OpenCV versions
    contours = contours[0] if imutils.is_cv2() else contours[1]

    letter_image_regions = []

    # 现在我们可以遍历四个轮廓中的每一个，并提取字母
    # inside of each one
    for contour in contours:
        #调用cv2.boundingRect函数，获取包含该边界的最小矩形边框
        (x, y, w, h) = cv2.boundingRect(contour)
        # 比较轮廓的宽度和高度以检测联合成一个块的字母
        if w / h > 1.25:
            #太宽了，不可能只是一个字幕
            # This contour is too wide to be a single letter!
            # Split it in half into two letter regions!
            half_width = int(w / 2)
            letter_image_regions.append((x, y, half_width, h))
            letter_image_regions.append((x + half_width, y, half_width, h))
        else:
            # This is a normal letter by itself
            letter_image_regions.append((x, y, w, h))

    # 如果抽取的字母超出4个，则放弃该图片(不要坏的数据)
    if len(letter_image_regions) != 4:
        continue
    # 根据x坐标对检测到的字母图像进行排序，以确保我们正在从左到右地处理它们，
    # 以便我们将正确的图像与正确的字母相匹配
    # sorted排序函数，这里根据关键字key排序，key我们定义的是每个矩形框的第一个元素(x的位置大小)
    letter_image_regions = sorted(letter_image_regions, key=lambda x: x[0])

    # Save out each letter as a single image
    for letter_bounding_box, letter_text in zip(letter_image_regions, captcha_correct_text):
        # 获取图像中字母的坐标
        x, y, w, h = letter_bounding_box

        # 从原始图像中提取边缘周围的2像素边距的字母
        letter_image = gray[y - 2:y + h + 2, x - 2:x + w + 2]

        # 获取文件夹以保存图像
        save_path = os.path.join(OUTPUT_FOLDER, letter_text)

        # if the output directory does not exist, create it
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        # write the letter image to a file
        # 字典的get函数，如果字典中不存在，tletter_text则创建一个新的，默认值设置为1，
        # 如果已经存在，则返回对应的值。
        count = counts.get(letter_text, 1)
        p = os.path.join(save_path, "{}.png".format(str(count).zfill(6)))
        cv2.imwrite(p, letter_image)

        # increment the count for the current key
        counts[letter_text] = count + 1
