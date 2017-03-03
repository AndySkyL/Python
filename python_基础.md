##Python 基础
-------------------------------------

###输入输出
#####输出
使用print()可以向屏幕上输出指定的文字：

```
>>> print('Hello world!')  
Hello world!
```
print()中可以接受多个字符串，当用逗号隔开时会形成一连串的输出,逗号相当于空格：

```
>>> print('I','LOVE','Python')
I LOVE Python
```
print()也可以用于计算：

```
>>> print(100+100)
200
>>> print('100 + 100 =',100+100)
100 + 100 = 200
```
#####输入
input()可以让用户输入字符：

```
>>> aa=input()
Python
>>> aa
'Python'
```

###字符串编码
* ASCII:使用一个字节，此编码包含大小写英文字母，数字符号等。
* Unicode：一般使用两个字节表示字符，可表示所有语言字符。
> 在使用Unicode表示ASCII字符的时候，只需要在二进制的ASCII码前补0即可。
* UTF-8：可变长编码。将一个Unicode字符根据不同的数字大小转化成1-6个字节，通常英文被转化为1个字节，汉字通常是3个字节。
> 在保存和传输文件时为了节省空间都会转化为UTF-8的字符编码格式，当需要在内存中加载时再转化为Unicode编码。

#####转化函数
可以使用ord()和chr()函数对字符和编码进行转换：

```
>>> ord('A')
65
>>> ord('中') 
20013
>>> chr(66)
'B'
>>> chr(25991)
'文'
```
也可以使用16进制的表示：

```
>>> '\u4e2d\u6587'
'中文'
```


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
    

* break 用来结束循环
* continue 跳过当前的循环，继续下一次循环
 > break语句可以在循环过程中直接退出循环，而continue语句可以提前结束本轮循环，并直接开始下一轮循环。这两个语句通常都必须配合if语句使用。不要滥用break和continue语句。break和continue会造成代码执行逻辑分叉过多，容易出错。大多数循环并不需要用到break和continue语句，上面的两个例子，都可以通过改写循环条件或者修改循环逻辑，去掉break和continue语句。
 
####dict和set
Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。

```
>>> aa={'a':1,'b':2,'c':3}
>>> aa['b']
2
```
1. 把数据放入dict的方法，除了初始化时指定外，还可以通过key放入。由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉：

   
   ```
   >>> aa['a']=100
   >>> aa['a']
   100
   ```
   
* 如果key不存在，dict就会报错：
  
  ```
  >>> aa['d']
  Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  KeyError: 'd'
  ```
* 可以通过如下两种方法判断KEY值是否存在：
  * 使用`in`判断key值是否存在：
    
    ```
    >>> 'd' in aa
    False
    >>> 'a' in aa 
    True
    ```
  * 通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value：
    
    ```
    >>> aa.get('c','xx')
    3
    >>> aa.get('d','xx')
    'xx'
    >>> aa.get('d')     
    >>> 
    ```
  * 要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
    
    ```
    >>> aa.pop('c')
	3
	>>> aa.get('c')
	>>>
	>>> aa
    {'a': 100, 'b': 2} 
    ```
  注意： dict内部存放的顺序和key放入的顺序是没有关系的。

* 和list比较，dict有以下几个特点：
  * 查找和插入的速度极快，不会随着key的增加而变慢；
  * 需要占用大量的内存，内存浪费多。
* list有与之相反的特性：
  * 查找和插入的时间随着元素的增加而增加；
  * 占用空间小，浪费内存很少。
  
> 提示：dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。

> 要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key.

######set
set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，而且元素是无序的，所以，在set中，没有重复的key。
要创建一个set，需要提供一个list作为输入集合：

```
>>> s = set([1, 2, 3])
>>> s
{1, 2, 3}
```
重复元素在set中自动被过滤：

```
>>> s = set([1, 1, 2, 2, 3, 3])
>>> s
{1, 2, 3}
```

通过remove(key)方法可以删除元素：

```
>>> s.remove(4)
>>> s
{1, 2, 3}
```
set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：

```
>>> s1 = set([1, 2, 3])
>>> s2 = set([2, 3, 4])
>>> s1 & s2
{2, 3}
>>> s1 | s2
{1, 2, 3, 4}
```
set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。

```
>>> a
{8, 9, 10}
>>> a.add(list)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
```

###函数

1. 几个常用的函数：
   * abs() 求绝对值
   * max() 返回最大的值
   * int() 转换为int类型
   * float() 转换为浮点数
   * str() 转换为字符串
   * bool() 转换为布尔，1为 True,空为False
   * hex() 转换整数为16进制表示的字符串
2. 定义函数
   
   ```
   >>> def my_fun(x):
   ...     if x > 0:
   ...         return x
   ...     else:
   ...         return -x
   ... 
   >>> my_fun(9)
   9
   >>> my_fun(-8)
   8
    ```

   > 如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。return None可以简写为return。

3. 如果要调用另一个文件中的函数，可以在文件开头加上：`from FILE_NAME import FUN_NAME`
4. 如果想定义一个什么事情都不做的空函数可以用`pass`这样可以防止报错（同理，也可以放在空语句中）:
   
   ```
   def nop():
       pass
   ```
