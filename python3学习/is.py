ques=['name','sexual']
anser=['ljn','man']
for q,a in zip(ques,anser):
    print(f'What is your {q}?  It is {a}.')
name='xiaoming'
age=10
print ("我叫 %s 今年 %d 岁!" % (name, age))
print ("我叫 {1} 今年 {0} 岁!!!".format(name,age))
print(f"我叫{name},今年{age}岁")
a=range(1,10)
print(type(a))
print(a)
b=list(a)
print(b)
print(list(range(1,11)))

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
set1=set(basket)
print(set1)
print(sorted(set1))

