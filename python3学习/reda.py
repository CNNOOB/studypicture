try:
	raise NameError('HiThere')  # 模拟一个异常。
except NameError:
        print('An exception flew by!')
        raise
