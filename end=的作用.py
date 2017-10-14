#  end传递一个空字符串，这样print函数不会在字符串末尾添加一个换行符

count = 3
password = 'FishC.com'
while count:
	passwd = input('请输入密码：')
	count -= 1
	if passwd == password:
		print('密码输入正确，进入程序。。。')
		break
	elif '*' in passwd:
		print('密码中不能含有"*"号！您还有',count,'次机会',end = '')
		continue
	else:
		print('密码输入错误，您还有：',count,'次机会')