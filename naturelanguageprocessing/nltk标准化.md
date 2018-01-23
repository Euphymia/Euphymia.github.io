# 使用nltk标准化文本

---

> * 消除标点符号
> * 文本大小写切换
> * 使用停止词
> * 相似度度量

---

## 代码

```python
import nltk
#消除标点符号
text=[" It is a pleasant evening.","Guests, who came from US arrived at the venue","Food was tasty."]
#先使用 word_tokenize将每句话切分成单词及符号
from nltk.tokenize import word_tokenize
tokenized_docs=[word_tokenize(doc) for doc in text]
print(tokenized_docs)
#>>>[['It', 'is', 'a', 'pleasant', 'evening', '.'], ['Guests', ',', 'who', 'came', 'from', 'US', 'arrived', 'at', 'the', 'venue'], ['Food', 'was', 'tasty', '.']]
#从切分后的文本中删除标点符号
import re
import string
#创建re模式对象
#string.punctuation 返回所有的特护符号
print(string.punctuation)
#>>>!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
x=re.compile('[%s]' % re.escape(string.punctuation))
tokenized_docs_no_punctuation = []
for review in tokenized_docs:
    new_review = []
    for token in review: 
        #sub是substitute，表示替换    
        new_token = x.sub(u'', token)
        if not new_token == u'':
            new_review.append(new_token)
    tokenized_docs_no_punctuation.append(new_review)	
print(tokenized_docs_no_punctuation)
#>>>[['It', 'is', 'a', 'pleasant', 'evening'], ['Guests', 'who', 'came', 'from', 'US', 'arrived', 'at', 'the', 'venue'], ['Food', 'was', 'tasty']]
#文本的大小写切换
text='HARdWork IS KEy to SUCCESS'
print(text.lower())
#>>>hardwork is key to success
print(text.upper())
#>>>HARDWORK IS KEY TO SUCCESS
#使用停止词，删除一些特别常用，没多大意义的词
from nltk.corpus import stopwords
#选择英文停止词库
stops=set(stopwords.words('english'))
words=["Don't", 'hesitate','to','ask','questions']
print([word for word in words if word not in stops])
#>>>["Don't", 'hesitate', 'ask', 'questions']
#相似性度量
from nltk.metrics import *
training='PERSON OTHER PERSON OTHER OTHER ORGANIZATION'.split()
testing='PERSON OTHER OTHER OTHER OTHER OTHER'.split()
print(accuracy(training,testing))
#>>>0.6666666666666666
trainset=set(training)
testset=set(testing)
print(precision(trainset,testset))
#>>>1.0
print(recall(trainset,testset))
#>>>0.6666666666666666
#f_measure 是precision和recall 的均值    
print(f_measure(trainset,testset))
#>>>0.8
import nltk
#通过距离判断相似性
from nltk.metrics import *
print(edit_distance("relate","relation"))
#>>>3
print(edit_distance("suggestion","calculation"))
#>>>7
#使用Jaccard系数执行相似性度量
#判断两个集合交集的相似性程度
from nltk.metrics import *
X=set([10,20,30,40])
Y=set([20,30,60])
print(jaccard_distance(X,Y))
#>>>0.6
#二进制距离判断相似度，如果两个标签相同返回0.0，否则返回1.0
from nltk.metrics import *
X = set([10,20,30,40])
Y= set([30,50,70])
print(binary_distance(X, Y))
#>>>1.0
```

