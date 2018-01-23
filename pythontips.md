# Python Tips

---

> * format

---

## format

用法：

　　它通过{}和:来代替传统%方式

1、使用位置参数

要点：从以下例子可以看出位置参数不受顺序约束，且可以为{},只要format里有相对应的参数值即可,参数索引从0开，传入位置参数列表可用*列表

```python
>>> li = ['hoho',18]
>>> 'my name is {} ,age {}'.format('hoho',18)
'my name is hoho ,age 18'
>>> 'my name is {1} ,age {0}'.format(10,'hoho')
'my name is hoho ,age 10'
>>> 'my name is {1} ,age {0} {1}'.format(10,'hoho')
'my name is hoho ,age 10 hoho'
>>> 'my name is {} ,age {}'.format(*li)
'my name is hoho ,age 18'

```

2、使用关键字参数

要点：关键字参数值要对得上，可用字典当关键字参数传入值，字典前加**即可

```python
>>> hash = {'name':'hoho','age':18}
>>> 'my name is {name},age is {age}'.format(name='hoho',age=19)
'my name is hoho,age is 19'
>>> 'my name is {name},age is {age}'.format(**hash)
'my name is hoho,age is 18'
```

3、填充与格式化:

(填充字符)(对齐方式 <^>)[宽度]

```python
>>> '{0:*>10}'.format(10)  ##右对齐
'********10'
>>> '{0:*<10}'.format(10)  ##左对齐
'10********'
>>> '{0:*^10}'.format(10)  ##居中对齐
'****10****'
```

