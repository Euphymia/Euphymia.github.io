# 利用nltk切分文本

---

> * 将文本切分为语句
> * 将句子切分为单词
> * 使用正则表达式实现切分
> * 使用split划分单词和句子

---

## 代码实现

```python
import nltk
#将文本切分为语句
text = "welcome readers. I hope you find it interesting. Please do reply."
from nltk.tokenize import sent_tokenize
print(sent_tokenize(text))
#>>>['welcome readers.', 'I hope you find it interesting.', 'Please do reply.']
##切分大量语句
tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
print(type(tokenizer))
#>>><class 'nltk.tokenize.punkt.PunktSentenceTokenizer'>
print(tokenizer.tokenize(text))
#>>>['welcome readers.', 'I hope you find it interesting.', 'Please do reply.']
#其它语言文本的划分
#加载它们各自的pickle文件（tokenizers/punkt里面找到）
#下面切分法语文本
french_tokenizer = nltk.data.load("tokenizers/punkt/french.pickle")
print(french_tokenizer.tokenize('Deux agressions en quelques jours, voilà ce qui a motivé hier matin le débrayage  collège franco-britanniquedeLevallois-Perret. Deux agressions en quelques jours, voilà ce qui a motivé hier matin le débrayage  Levallois. L’équipe pédagogique de ce collège de 750 élèves avait déjà été choquée par l’agression, janvier , d’un professeur d’histoire. L’équipe pédagogique de ce collège de 750 élèves avait déjà été choquée par l’agression, mercredi , d’un professeur d’histoire'))
#>>>['Deux agressions en quelques jours, voilà ce qui a motivé hier matin le débrayage  collège franco-britanniquedeLevallois-Perret.', 'Deux agressions en quelques jours, voilà ce qui a motivé hier matin le débrayage  Levallois.', 'L’équipe pédagogique de ce collège de 750 élèves avait déjà été choquée par l’agression, janv
# ier , d’un professeur d’histoire.', 'L’équipe pédagogique de ce collège de 750 élèves avait déjà été choquée par l’agression, mercredi , d’un professeur d’h
# istoire']
#将句子切分为单词(基于空格和标点符号，只能是一个句子)
text = nltk.word_tokenize("PierreVinken , 59 years old , will join as a nonexecutive director on Nov. 29 .")
print(text)
#>>>['PierreVinken', ',', '59', 'years', 'old', ',', 'will', 'join', 'as', 'a', 'nonexecutive', 'director', 'on', 'Nov.', '29', '.']
#使用WordPunctTokenizer切分单词
from nltk.tokenize import WordPunctTokenizer
tokenizer = WordPunctTokenizer()
print(tokenizer.tokenize("Don't hesitate to ask questions"))
#>>>['Don', "'", 't', 'hesitate', 'to', 'ask', 'questions']
#使用正则表达式实现切分
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer("[\w']+")
print(tokenizer.tokenize("Don't hesitate to ask questions"))
#>>>["Don't", 'hesitate', 'to', 'ask', 'questions']
sent=" She secured 90.56 % in class X . She is a meritorious student"
print(tokenizer.tokenize(sent))
#识别不出来特殊符号 %
#>>>['She', 'secured', '90', '56', 'in', 'class', 'X', 'She', 'is', 'a', 'meritorious', 'student']
#筛选大写字母开头的单词
from nltk.tokenize import RegexpTokenizer
capt = RegexpTokenizer("[A-Z]\w+")
sent=" She secured 90.56 % in class X . She is a meritorious student"
print(capt.tokenize(sent))
#>>>['She', 'She']
#使用 split方法进行划分
sent=" She secured 90.56 % in class X . She is a meritorious student"
print(sent.split())
#>>>['She', 'secured', '90.56', '%', 'in', 'class', 'X', '.', 'She', 'is', 'a', 'meritorious', 'student']
print(sent.split(' '))
#>>>['', 'She', 'secured', '90.56', '%', 'in', 'class', 'X', '.', 'She', 'is', 'a', 'meritorious', 'student']
sent=" She secured 90.56 % in class X\n . She is a meritorious student"
#使用split('\n')划分句子
print(sent.split('\n'))
#>>>[' She secured 90.56 % in class X . She is a meritorious student']
```

