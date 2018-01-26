#使用NLTK处理形态学与词性标注

---

> * stem()词干提取
> * check()形态分析
> * pos_tag()词性标注
> * FreqDist()统计频率
> * name语料库
> * n-gram统计建模
> * 使用词性标注语料库开发分块器

---

##简单介绍：

**词干提取**：nltk给出的词干提取器有很多种，各有各的优点，这里用到了PorterStemmer和LancasterStemmer两种。Lancaster涉及更多不同情感词的使用。

**形态分析：**由于在win系统上没有64位的pyenchant可用，所以没试验，不过大致作用为单词识别，单词拼写检查等等，比如这里的例子，可将输入的'ilikeyou'识别成'i like you'

**词性标注：**给每个单词标注上它的词性，如名词，动词，代词等等。也可以取消标注，设置默认标注，将标注二元组转换成一个字符串或反过来。

**统计频率：**使用nltk的FreqDist函数用于统计不同单词出现的个数

**name语料库：**nltk.corpus里又一个name的函数，它可以调用’male.txt'和'female.txt'两个名字语料库

**n-gram统计建模：**这里使用的一元统计建模，二元统计建模和n元统计建模。训练，并测试它们执行词性标注的准确性。

##代码

```python
#PorterStemmer词干提取
import nltk
from nltk.stem import PorterStemmer
stemmerporter=PorterStemmer()
print(stemmerporter.stem('working'))
#>>>work
print(stemmerporter.stem('happiness'))
#>>>happi
#Lancaster词干提取器，比Porter涉及更多不同情感词的使用
from nltk.stem import LancasterStemmer
stemmerlan=LancasterStemmer()
print(stemmerlan.stem('working'))
#>>>work
print(stemmerlan.stem('happiness'))
#>>>happy


# 形态分析
# 由于enchant不能用于64位win系统上，没有试验
# import enchant
# s = enchant.Dict("en_US")
# tok=[]
# def tokenize(str1):
#     if not str1: return
#     for j in xrange(len(str1),-1,-1):
#         if s.check(str1[0:j]):
#             tok.append(str1[0:j])
#             str1=str1[j:]
#             tokenize(st1)
#             break
# tokenize('itismyfavouratebook')
# print(tok)


#词性标注
text1=nltk.word_tokenize("It is a pleasant day today")
print(nltk.pos_tag(text1))
#>>>[('It', 'PRP'), ('is', 'VBZ'), ('a', 'DT'), ('pleasant', 'JJ'), ('day', 'NN'), ('today', 'NN')]
text=nltk.word_tokenize("I cannot bear the pain of bear")
print(nltk.pos_tag(text))
#>>[('I', 'PRP'), ('can', 'MD'), ('not', 'RB'), ('bear', 'VB'), ('the', 'DT'), ('pain', 'NN'), ('of', 'IN'), ('bear', 'NN')]
#取消句子标注
from nltk.tag import untag
print(untag([('beautiful','NN'),('morning','NN')]))
#>>>['beautiful', 'morning']
#给所有的标识符分配同词性分配的标注
from nltk import DefaultTagger
tag=DefaultTagger('NN')
print(tag.tag(['beautiful','morning']))
#>>>[('beautiful', 'NN'), ('morning', 'NN')]
#现在将上述生成的元组(单词，词性)转换为一个字符串
taggedtok=('bear','NN')
#tuple2str 将元组转换成字符串
from nltk.tag.util import tuple2str
taggedword=tuple2str(taggedtok)
print(taggedword)
#>>>bear/NN
#str2tuple 将字符串转变成元组
taggedword=nltk.tag.str2tuple('bear/NN')
print(taggedword)
#>>>('bear', 'NN')


#获取Treebank语料库中的一些常用标记的出出现频率
from nltk.corpus import treebank
#获取已经目标集为'universal'标注的语料库
treebank_tagged = treebank.tagged_words(tagset='universal')
#按照tag词性统计频率
tag = nltk.FreqDist(tag for (word, tag) in treebank_tagged)
print(tag.most_common())    
#>>>[('NOUN', 28867), ('VERB', 13564), ('.', 11715), ('ADP', 9857), ('DET', 8725), ('X', 6613), 
#    ('ADJ', 6397), ('NUM', 3546), ('PRT', 3219), ('ADV', 3171), ('PRON', 2737), ('CONJ', 2265)]
#计算出现在一个名词之前的标记的数量
from nltk.corpus import treebank	
treebank_tagged = treebank.tagged_words(tagset='universal')
#获取二元组 将每两个元素组合在一起
tagpairs = nltk.bigrams(treebank_tagged)
#获取名词标记之前的标记
preceders_noun = [x[1] for (x, y) in tagpairs if y[1] == 'NOUN']
#获取名词标记之前的标记频率
freqdist = nltk.FreqDist(preceders_noun)
#只打印出freqdist前面标签的部分
print([tag for (tag, _) in freqdist.most_common()])
#>>>['NOUN', 'DET', 'ADJ', 'ADP', '.', 'VERB', 'NUM', 'PRT', 'CONJ', 'PRON', 'X', 'ADV']


#NLTK中有一个单词列表语料库叫做Names语料库，它分别包括male.txt与female.txt
from nltk.corpus import names
print(len(names.words('male.txt')))
#>>>2943
print(names.words('male.txt')[:10])
#>>>['Aamir', 'Aaron', 'Abbey', 'Abbie', 'Abbot', 'Abbott', 'Abby', 'Abdel', 'Abdul', 'Abdulkarim']
print(len(names.words('female.txt')))
#>>>5001
#NLTK也囊括了一个大的英文单词集
from nltk.corpus import words
print(words.fileids())
#>>>['en', 'en-basic']
print(len(words.words('en')))
#>>>235886
print(words.words('en')[0:10])
#>>>['A', 'a', 'aa', 'aal', 'aalii', 'aam', 'Aani', 'aardvark', 'aardwolf', 'Aaron']
print(len(words.words('en-basic')))
#>>>850


#涉及 n—gram的统计建模
from nltk.tag import UnigramTagger
from nltk.corpus import treebank
#获取Treebank语料库的前7000个句子
training= treebank.tagged_sents()[:7000]
#在初始化标注器时提供一个句子的列表来执行UnigramTagger的训练,UnigramTagger为一元语法标注器
unitagger=UnigramTagger(training)
#打印treebank中第一个句子
print(treebank.sents()[0])
#>>>['Pierre', 'Vinken', ',', '61', 'years', 'old', ',',
#    'will', 'join', 'the', 'board', 'as', 'a', 'nonexecutive', 'director', 'Nov.', '29', '.']
print(unitagger.tag(treebank.sents()[0]))
#>>>[('Pierre', 'NNP'), ('Vinken', 'NNP'), (',', ','), ('61', 'CD'), ('years', 'NNS'), ('old', 'JJ'),
#    (',', ','), ('will', 'MD'), ('join', 'VB'), ('the', 'DT'), ('board', 'NN'), ('as', 'IN'), ('a', 'DT'), 
#    ('nonexecutive', 'JJ'), ('director', 'NN'), ('Nov.', 'NNP'), ('29', 'CD'), ('.', '.')]
#评估UnigramTagger，计算其准确性
testing = treebank.tagged_sents()[2000:]
#evaluate：将测试结果与真实标签比较，返回测试结果的正确率
print(unitagger.evaluate(testing))
#>>>0.9619024159944167
#我们可以用一个特定的标记映射上下文键
#如下所示，只有'Vinken'对应的是'NN' 其它没指定的键都为None
unitag = UnigramTagger(model={'Vinken': 'NN'})
print(unitag.tag(treebank.sents()[0]))
#>>>[('Pierre', None), ('Vinken', 'NN'), (',', None), ('61', None), ('years', None), ('old', None), (',', None),
#    ('will', None), ('join', None), ('the', None), ('board', None), ('as', None), ('a', None), ('nonexecutive', None),
#    ('director', None), ('Nov.', None), ('29', None), ('.', None)]
from nltk.tag import UnigramTagger
from nltk.tag import DefaultTagger
from nltk.corpus import treebank
print(len(treebank.tagged_sents()))
testing = treebank.tagged_sents()[2000:]
training= treebank.tagged_sents()[:7000]
#设置默认标识符
tag1=DefaultTagger('NN')
#添加回退机制，如果UnigramTagger不能标注，就用tag1(默认标注)进行标注
tag2=UnigramTagger(training,backoff=tag1)
print(tag2.evaluate(testing))
#>>>0.9619024159944167
#使用BigramTagger，使用两个标记作为上下文信息
from nltk.tag import BigramTagger
from nltk.corpus import treebank
training_1= treebank.tagged_sents()[:7000]
#BigramTagger，二元标记训练器
bigramtagger=BigramTagger(training_1)
#打印出treebank.sents的第一个句子
print(treebank.sents()[0])
#>>>['Pierre', 'Vinken', ',', '61', 'years', 'old', ',', 'will', 'join', 'the', 'board',
#  'as', 'a', 'nonexecutive', 'director', 'Nov.', '29', '.']
#打印出打上词性标记的第一个句子
print(bigramtagger.tag(treebank.sents()[0]))
#>>>[('Pierre', 'NNP'), ('Vinken', 'NNP'), (',', ','), ('61', 'CD'), ('years', 'NNS'), ('old', 'JJ'), 
#    (',', ','), ('will', 'MD'), ('join', 'VB'), ('the', 'DT'), ('board', 'NN'), ('as', 'IN'), ('a', 'DT'), 
#    ('nonexecutive', 'JJ'), ('director', 'NN'), ('Nov.', 'NNP'), ('29', 'CD'), ('.', '.')]
testing_1 = treebank.tagged_sents()[2000:]
#打印出使用两个标记作为上下文信息的准确度
print(bigramtagger.evaluate(testing_1))
#>>>0.9171131227292321
#tnt 代表Trigrams n Tags。TnT建立在二阶马尔科夫模型的基础上，是一个基于统计的标注器
#为了选择最佳模型，tnt使用了n元语法模型
from nltk.tag import tnt
from nltk.corpus import treebank
testing = treebank.tagged_sents()[2000:]
training= treebank.tagged_sents()[:7000]
tnt_tagger=tnt.TnT()
tnt_tagger.train(training)
# print(tnt_tagger.evaluate(testing))
#需要花费很长的时间，但是正确率很高
#>>>0.9882176652913768
```

##使用词性标注语料库开发分块器

1.正则表达式分块器，将一个或多个连续的词分成一块。 分块是用于实体识别的基本技术。

名词短语分块：名词短语分块也叫做NP-分块，NP-分块信息最有用的来源之一是词性标记，所以我们一般在分块前都会进行词性标注。

| 符号   | 含义                | 例子                      |
| ---- | ----------------- | ----------------------- |
| S    | sentence          | the man walked          |
| NP   | noun phrase(名词短语) | a dog                   |
| VP   | verb phrase       | saw a park              |
| PP   | prepositional     | phrase with a telescope |
| Det  | determiner        | the                     |
| N    | noun              | dog                     |
| V    | verb              | walked                  |
| P    | preposition       | in                      |

2.评估分块器

块在文本文件中的标准方式是IOB标记：I（inside，内部），O（outside，外部），B（begn，开始）

3.使用一元标注器创建分块器并评估。

## 代码

```python
import nltk

# 自己定义一个分词
text = "Lucy let down her long golden hair"
#将句子拆分成单词
sentence = nltk.word_tokenize(text)

# 词性标注
sentence_tag = nltk.pos_tag(sentence)
print(sentence_tag)
#>>>[('Lucy', 'NNP'), ('let', 'VBD'), ('down', 'RP'), ('her', 'PRP$'), ('long', 'JJ'), ('golden', 'JJ'), ('hair', 'NN')]
# 定义分块语法
# JJ表示形容词，DT限定词，PRP$所有格式代词，NN名词，IN介词，NNP专有名词
# 第一条规则匹配可选的词（限定词或格代名词），零个或多个形容词，然后跟一个名词
# 第二条规则匹配一个或多个专有名词
# $符号是正则表达式中的一个特殊字符，必须使用转义符号\来匹配PP$
grammar = r"""
    NP: {<DT|PRP\$>?<JJ>*<NN>}
        {<NNP>+}
"""

# 进行分块
cp = nltk.RegexpParser(grammar)
tree = cp.parse(sentence_tag)
tree.draw()


#另一种复杂的情况：加缝隙
import nltk

# 分词
text = "the little yellow dog barked at the cat"
sentence = nltk.word_tokenize(text)
# 词性标注
sentence_tag = nltk.pos_tag(sentence)
print(sentence_tag)
#>>>[('the', 'DT'), ('little', 'JJ'), ('yellow', 'JJ'), ('dog', 'NN'), ('barked', 'VBD'), ('at', 'IN'), ('the', 'DT'), ('cat', 'NN')]

# 定义缝隙语法
# 第一个规则匹配整个句子
# 第二个规则匹配一个或多个动词或介词
# 一对}{就代表把其中语法匹配到的词作为缝隙
grammar = r"""
NP: {<.*>+}
    }<VBD|IN>+{
"""
cp = nltk.RegexpParser(grammar)

# 分块 NLTK Tree
tree = cp.parse(sentence_tag)
tree.draw()

# 评估分块器
# 块在文本文件中的标准方式是IOB标记：I（inside，内部），O（outside，外部），B（begn，开始）
# conll2000语料库
import nltk
from nltk.corpus import conll2000

# 加载训练文本中的NP块，返回的结果可以当作是一个列表，列表中的元素是Tree对象
# 每一个Tree对象就是一个被分块的句子
test_sents = conll2000.chunked_sents("train.txt", chunk_types=["NP"])

# tree2conlltags函数可以将Tree对象转换为IBO标记格式的列表
tags = nltk.chunk.tree2conlltags(test_sents[0])
print(tags)
#>>>[('Confidence', 'NN', 'B-NP'), ('in', 'IN', 'O'), ('the', 'DT', 'B-NP')....]

# 查找以名词短语标记的特征字母（如CD、DT 和JJ）开头的标记
grammar = r"NP: {<[CDJNP].*>+}"
cp = nltk.RegexpParser(grammar)

# 加载训练文本中的NP块
test_sents = conll2000.chunked_sents("train.txt", chunk_types=["NP"])
print(cp.evaluate(test_sents))
#>>>ChunkParse score:
    # IOB Accuracy:  87.4%%
    # Precision:     69.7%%
    # Recall:        67.5%%
    # F-Measure:     68.6%%

class UnigramChunker(nltk.ChunkParserI):
    """
    一元分块器，
    该分块器可以从训练句子集中找出每个词性标注最有可能的分块标记，
    然后使用这些信息进行分块
    """
    def __init__(self, train_sents):
        """
        构造函数
        :param train_sents: Tree对象列表
        """
        train_data = []
        for sent in train_sents:
            # 将Tree对象转换为IOB标记列表[(word, tag, IOB-tag), ...]
            conlltags = nltk.chunk.tree2conlltags(sent)

            # 找出每个词性标注对应的IOB标记
            ti_list = [(t, i) for w, t, i in conlltags]
            train_data.append(ti_list)

        # 使用一元标注器进行训练
        self.__tagger = nltk.UnigramTagger(train_data)

    def parse(self, tokens):
        """
        对句子进行分块
        :param tokens: 标注词性的单词列表
        :return: Tree对象
        """
        # 取出词性标注
        tags = [tag for (word, tag) in tokens]
        # 对词性标注进行分块标记
        ti_list = self.__tagger.tag(tags)
        # 取出IOB标记
        iob_tags = [iob_tag for (tag, iob_tag) in ti_list]
        # 组合成conll标记
        conlltags = [(word, pos, iob_tag) for ((word, pos), iob_tag) in zip(tokens, iob_tags)]

        return nltk.chunk.conlltags2tree(conlltags)

test_sents = conll2000.chunked_sents("test.txt", chunk_types=["NP"])
train_sents = conll2000.chunked_sents("train.txt", chunk_types=["NP"])

unigram_chunker = UnigramChunker(train_sents)
print(unigram_chunker.evaluate(test_sents))
#>>>ChunkParse score:
    # IOB Accuracy:  92.9%%
    # Precision:     79.9%%
    # Recall:        86.8%%
    # F-Measure:     83.2%%
```

