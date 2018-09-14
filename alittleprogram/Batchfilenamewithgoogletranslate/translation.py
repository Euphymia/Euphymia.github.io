from GoogleFreeTrans import Translator
translator = Translator.translator()
# print(translator.translate(
#     'A Generative Approach to Zero-Shot and Few-Shot Action Recognition'))

import os
import sys
path0 = r"C:\Users\think\Desktop\零样本学习"
path1 = r"C:\Users\think\Desktop\零样本学习"+'\\'

sys.path.append(path1)
print(sys.path)

# 列出当前目录下所有的文件
files = os.listdir(path0)

# files = os.listdir('.')

print('files', files)

for filename in files:
    portion = os.path.splitext(filename)
    print(portion[0])
    # 如果后缀是.txt
    if portion[1] == ".pdf":
        # 重新组合文件名和后缀名
        temp=translator.translate(portion[0])
        newname = temp + ".pdf"
        filenamedir = path1 + filename
        newnamedir = path1+newname

        # os.rename(filename,newname)
        os.rename(filenamedir, newnamedir)
