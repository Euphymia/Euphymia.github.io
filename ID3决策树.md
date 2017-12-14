# ID3决策树

标签（空格分隔）： 机器学习算法

---

> * 心得
> * 代码（调用test（）即可使用）

---

##心得
    决策树与K近邻算法不同，它需要根据预处理过的数据的建立分类器，然后将待测试数据直接带入建好的决策树中即可获得结果，建立决策树的过程，就是将原始杂乱的训练集变的更加有序，ID3的方法就是使用信息论的方法建立决策树，我们以信息增益是否最高作为选取某个特征划分数据的标准。数据集中数据既可以是数字也可以是字符串，并不影响计算。
    
##代码

```pyhton
from math import log
import operator

def createDataSet():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing','flippers']
    #change to discrete values
    return dataSet, labels

def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}#统计DataSet中存在标签类别及数量用于计算香农值
    for featVec in dataSet: #the the number of unique elements and their occurance
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys(): labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob * log(prob,2) #log base 2
    return shannonEnt

def splitDataSet(dataSet, axis, value):  #划分数据集,axis为划分的特征的列数，选出axis列中值为value的
    #选取dataSet第axis列中值为value的前后所有数据，并存入新列表中
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]     #chop out axis used for splitting
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet
    
def chooseBestFeatureToSplit(dataSet):#选取最好的数据集划分方式（信息增量最大）
    numFeatures = len(dataSet[0]) - 1      #the last column is used for the labels
    baseEntropy = calcShannonEnt(dataSet) #计算原始的香农熵
    bestInfoGain = 0.0; bestFeature = -1 #初始化最佳信息增量，最佳划分特征
    for i in range(numFeatures):        #iterate over all the features
        featList = [example[i] for example in dataSet]#将第i列的特征值组成一个新的列表
        uniqueVals = set(featList)       #获取新列表的所有存在的类别（用于创建新子树）
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)#利用splitDataSet函数，得到已dii列，value值划分的子数据集
            prob = len(subDataSet)/float(len(dataSet)) #计算划分出的数据占总数据的比重，用于算出总的香农熵
            newEntropy += prob * calcShannonEnt(subDataSet)#计算总香农熵
        infoGain = baseEntropy - newEntropy     #计算信息增量
        if (infoGain > bestInfoGain):       #compare this to the best gain so far
            bestInfoGain = infoGain         #保存最佳的分类特征
            bestFeature = i
    return bestFeature                      #returns an integer

def majorityCnt(classList):
    classCount={}
    for vote in classList:
        if vote not in classCount.keys(): classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

def createTree(dataSet,labels):#递归生成决策树
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) == len(classList): #列表的count方法返回某个元素在列表中出现的次数
        return classList[0]#当划分的数据集中所有元素标签都相等时即可停止划分
    if len(dataSet[0]) == 1: #数据集中只剩标签时直接选取标签最多的一类作为分类标签
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel:{}}
    del(labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]       #copy all of labels, so trees don't mess up existing labels
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value),subLabels)
    return myTree                            
    
def classify(inputTree,featLabels,testVec):
    #递归利用决策树得到分类结果，inputTree：建好的决策树，featLabels：标签列表，testVec：待测试数据
    firstStr = list(inputTree.keys())[0] #获取当前分类用的特征
    print(firstStr)
    secondDict = inputTree[firstStr] #获取该特征下可分的类别
    featIndex = featLabels.index(firstStr) #获取该特征对应的索引
    key = testVec[featIndex]
    valueOfFeat = secondDict[key] 
    if isinstance(valueOfFeat, dict): #如果valueOfFeat是字典表示还未分类完成，继续递归
        classLabel = classify(valueOfFeat, featLabels, testVec)
    else: classLabel = valueOfFeat#否则表示已分类完成
    return classLabel

def storeTree(inputTree,filename):
    #使用pickle模块储存决策树
    import pickle
    fw = open(filename,'wb+')
    pickle.dump(inputTree,fw)
    fw.close()
    
def grabTree(filename):
    #使用pickle模块获取决策树
    import pickle
    fr = open(filename,'rb')
    return pickle.load(fr)
    
def test():
    d,l=createDataSet()
    m=createTree(d,l)
    d,l=createDataSet()
    print(classify(m,l,[1,1]))
```

