def foo(x):
	tmp = [3]
	def ins(y):
		tmp[0] = tmp[0] + 1
		print(x+y+tmp[0])
	return ins

bar = foo(2)
bar2 = foo(2)
bar(10)
bar(10)
bar(10)
bar2(10)
bar2(10)