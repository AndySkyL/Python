##Python 基础
-------------------------------------
###list和tuple

#####list

1. list是一种有序的集合，可以随时添加和删除其中的元素。

   ```
   >>> a = ['a', 'b', 'c']
   >>> a
   ['a', 'b', 'c']
   ```

* 用`len()`函数可以获得list元素的个数：

	```
	>>> len(a)
	3
	```
* 用索引来访问list中每一个位置的元素，记得索引是从0开始的：

	```
	>>> a [0]
	'a'
	>>> a [2]
	'c'
	```
* 如果要取最后一个元素，除了计算索引位置外，还可以使用倒序的方式，用负数表示，最后一个为-1，直接获取最后一个元素：
	
	```
	>>> a[-1]
	'c'
	>>> a[-2]
    'b'
    ```

* list是一个可变的有序表，所以，可以往list中追加元素到末尾，使用`append（）`函数：
   
   ```
   >>> a.append('x')
   >>> a
   ['a', 'b', 'c', 'x']
   ```
* 指定索引位置插入,使用`insert(,)`函数：
  
  ```
  >>> a.insert(1,'y')
  >>> a
  ['a', 'y', 'b', 'c', 'x']
  ```
* 删除list末尾的元素，用`pop()`方法：
  
  ```
  >>> a.pop()
  'x'
  >>> a
  ['a', 'y', 'b', 'c']
  ```
* 删除指定位置的元素，用`pop(i)`方法，其中i是索引位置：
  
  ```
  >>> a.pop(1)
  'y'
  >>> a
  ['a', 'b', 'c']
  ```
* 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：
  
  ```
  >>> a[1]='hello'
  >>> a
  ['a', 'hello', 'c']
  ```
* list里面的元素的数据类型也可以不同，比如：
  
  ```
  >>> L = ['Apple', 123, True]
  ```
* list中还可以嵌套其他list,且可以是变量：
   
   ```
   >>> s = ['python', 'java', ['asp', 'php'], 'scheme']
   ```
   ```
   >>> p = ['asp', 'php']
   >>> s = ['python', 'java', p, 'scheme']
   ```
* 要拿到'php'可以写p[1]或者s[2][1]，因此s可以看成是一个二维数组，类似的还有三维、四维……数组，不过很少用到。

* 如果一个list中一个元素也没有，就是一个空的list，它的长度为0：
  
  ```
  >>> L = []
  >>> len(L)
  0  
  ```
  
#####tuple
另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改，它没有append()，insert()这样的方法。其他获取元素的方法和list是一样的，你可以正常地使用b[0]，b[-1]，但不能赋值成另外的元素。 

```
>>> b = ('a','b','c')
>>> b[1]
'b'
>>> b.append('x')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'append'
```
不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。

> tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来，比如：
  
  ```
  >>> t = (1, 2)
  >>> t
  (1, 2)
  ```
  
* 如果要定义一个空的tuple，可以写成()：
  
  ```
  >>> t = ()
  >>> t
  ()
  ```
  
* 只有1个元素的tuple定义时必须加一个逗号,，来消除歧义,如果不加逗号，相当于赋值运算：
  
  ```
  >>> t = (1,)
  >>> t
  (1,)
  ```
* 在tuple中定义list,那么tuple中的list部分就是可变的：
  
  ```
  >>> t = ('a', 'b', ['A', 'B'])
  >>> t[2][0] = 'X'
  >>> t[2][1] = 'Y'
  >>> t
  ('a', 'b', ['X', 'Y'])
  ```
  

###条件语句

1. if ... else 条件判断：
   
   ```
   if <条件判断1>:
    <执行1>
   elif <条件判断2>:
    <执行2>
   elif <条件判断3>:
    <执行3>
   else:
    <执行4>
   ```
   示例(缩进敏感，默认使用4个空格)：
   
   ```
   age = 3
   if age >= 18:
       print('adult')
   elif age >= 6:
       print('teenager')
   else:
       print('kid')
   ```
   if语句执行有个特点，它是从上往下判断，如果在某个判断上是True，把该判断对应的语句执行后，就忽略掉剩下的elif和else：
   
   ```
   age = 20
   if age >= 6:
       print('teenager')
   elif age >= 18:
       print('adult')
   else:
       print('kid') 
   ```
   if判断条件还可以简写(`x`只要为非空的数值、字符串、list等，就判断为`True`,否则为`False`):
   
   ```
   if x:
       print('True')
   ``` 

* 循环语句
  
  * for 循环：
    
     ```
     sum = 0
     for x in range(101):
         sum = sum + x
     print(sum)
     ```
     `rang()`函数可以生成一个序列，使用`list（）`可以转换为list: 
     
     ```
     >>> list(range(5))
     [0, 1, 2, 3, 4]
     ```
     
     
     
  * while循环：
    
    ```
    sum = 0
    n = 99
    while n > 0:
        sum = sum + n
        n = n - 2
    print(sum) 
    ```
    

* break
