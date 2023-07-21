# Java Script学习
## 正则表达式
**参考链接**[菜鸟教程](https://www.runoob.com/jsref/jsref-obj-regexp.html)
### 修饰符
/i	忽略大小写


/g	执行全局匹配（查找所有匹配而非在找到第一个匹配后停止

/m	执行多行匹配。	

### 匹配函数
str.replace(patt,new str)返回替换后的字符串

str.search(patt)返回匹配的起始位置

str.match(patt) 返回匹配的结果，可以是数组

patt.exec(str)返回匹配结果，如果有多个匹配结果，每次调用exec会更新lastIndx

patt.test(str)返回true或false

## let和var和const
[菜鸟教程](https://www.runoob.com/js/js-let-const.html)

const定义常量与使用let 定义的变量相似：

* 二者都是块级作用域

* 都不能和它所在作用域内的其他变量或函数拥有相同的名称

两者还有以下两点区别：

* const声明的常量必须初始化，而let声明的变量不用

* const 定义常量的值不能通过再赋值修改，也不能再次声明。而 let 定义的变量值可以修改。

## DOM事件
[菜鸟教程](https://www.runoob.com/jsref/dom-obj-event.html)

## 数组和字符串操作
###数组
* 1.splice	从数组中添加或删除元素。
* 2.slice		选取数组的一部分，并返回一个新数组

### 字符串
* 1.slice		提取字符串的片断，并在新的字符串中返回被提取的部分。splice(begin,end)左包含，右不包含
* 2.split		把一个字符串分割成字符串数组

## 常犯错误
* 1.switch 语句会使用恒等计算符(===)进行比较

* 2.JavaScript 中的所有数据都是以 64 位浮点型数据(float) 来存储。

所有的编程语言，包括 JavaScript，对浮点型数据的精确度都很难确定：

``` 
var x = 0.1;
var y = 0.2;
var z = x + y            // z 的结果为 0.30000000000000004
if (z == 0.3)            // 返回 false
z = (x * 10 + y * 10) / 10;       // z 的结果为 0.3
```

* 3.null和undefined

``` 
typeof undefined             // undefined
typeof null                  // object
null === undefined           // false
null == undefined            // true
```





 
