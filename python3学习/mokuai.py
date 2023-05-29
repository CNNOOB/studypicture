import sys,math
 
print('命令行参数如下:')
for i in sys.argv:
   print(i)
print('\n\nPython 路径为：', sys.path, '\n')

s='hello world'
print(str(s))
print(repr(s))
print(type(repr(s)))
a=repr((1, 2, ('Google', 'Runoob')))
b=str((1, 2, ('Google', 'Runoob')))
print(a)
print(b)
print('--------------------------')
for x in range(1, 11):
	print(repr(x).rjust(2), repr(x*x).rjust(3),repr(x*x*x).rjust(4))
    # 注意前一行 'end' 的使用
	
for x in range(1,11):
	print(f'{x}.rjust(2),{x*x}.rjust(3),{x*x*x}.rjust(4)')


print('常量 PI 的值近似为： {!s}。'.format('123'))

table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
for name, number in table.items():
	print('{0:10} ==> {1:10d}'.format(name, number))
	print('{0:10} ==> {1:10}'.format(name, number))
print('--------------------------')
print('Runoob: {0[Runoob]:d}; Google: {0[Google]:d}; Taobao: {0[Taobao]:d}'.format(table))
print('Runoob: {Runoob:d}; Google: {Google:d}; Taobao: {Taobao:d}'.format(**table))
print('Runoob: {Runoob}; Google: {Google}; Taobao: {Taobao}'.format(**table))