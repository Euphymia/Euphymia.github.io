#根据extract_single_letters_from_caotchas.py生成的字母数据进行分类器训练
import cv2
import pickle
import os.path
import numpy as np
import h5py
from imutils import paths
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.layers.core import Flatten, Dense
from helpers import resize_to_fit

LETTER_IMAGES_FOLDER = "extracted_letter_images"
#保存训练结果
MODEL_FILENAME = "captcha_model.hdf5"
#保存标签
MODEL_LABELS_FILENAME = "model_labels.dat"


# initialize the data and labels
data = []
labels = []

# loop over the input images
# 获取LETTER_IMAGES_FOLDER路径下的所有照片的路径
for image_file in paths.list_images(LETTER_IMAGES_FOLDER):
    # Load the image and convert it to grayscale
    image = cv2.imread(image_file)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 为了加速训练
    # Resize the letter so it fits in a 20x20 pixel box
    image = resize_to_fit(image, 20, 20)
    # 在第三维增加一个维度    
    # Add a third channel dimension to the image to make Keras happy
    image = np.expand_dims(image, axis=2)

    # 根据所在文件夹抓取信件的名称
    # os.path.sep:路径分隔符 '/'
    # 例如'A/0011.png'.split('/')[-2] 
    # >>> A
    label = image_file.split(os.path.sep)[-2]

    # Add the letter image and it's label to our training data
    data.append(image)
    labels.append(label)


# 将原始像素强度缩放到范围[0,1]（这提高了训练）
data = np.array(data, dtype="float") / 255.0
labels = np.array(labels)

# Split the training data into separate train and test sets
(X_train, X_test, Y_train, Y_test) = train_test_split(data, labels, test_size=0.25, random_state=0)
# 将标签（字母）转换成Keras可以使用的单一编码
# 将标签二值化，即全部转换成0001000之类的二进制表示
# 这里只有32种标签(个别的没涉及，如0，1，O，,I等不好分类)，所以二值化后总共有32位
# 例如 '2'转换为 [1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
#     '3' 转换为 [0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
lb = LabelBinarizer().fit(Y_train)
Y_train = lb.transform(Y_train)
Y_test = lb.transform(Y_test)
 
# 保存从标签到单一编码的映射。
# 当我们使用模型解码预测意味着什么时，我们稍后需要这个
# 使用pickle.dump保存lb到当前文件夹
with open(MODEL_LABELS_FILENAME, "wb") as f:
    pickle.dump(lb, f)

# 建立一个神经网络(keras)
model = Sequential()

# First convolutional layer with max pooling
model.add(Conv2D(20, (5, 5), padding="same", input_shape=(20, 20, 1), activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

# Second convolutional layer with max pooling
model.add(Conv2D(50, (5, 5), padding="same", activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

# Hidden layer with 500 nodes
model.add(Flatten())
model.add(Dense(500, activation="relu"))

# Output layer with 32 nodes (one for each possible letter/number we predict)
model.add(Dense(32, activation="softmax"))

# Ask Keras to build the TensorFlow model behind the scenes
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

# Train the neural network
model.fit(X_train, Y_train, validation_data=(X_test, Y_test), batch_size=32, epochs=10, verbose=1)

# Save the trained model to disk
model.save(MODEL_FILENAME)
