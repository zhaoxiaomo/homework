#!/usr/bin/env python
# -*- coding:utf-8 -*-

#useing for login

#用户名和密码
users = {
	'zhao' : '123',
	'zhou' : '111',
	'he' : '222'
	}

user_stat = {
	'zhao' : 1,
	'zhou' : 1,
	'he' : 1
	}

i = 0

flag = False
while True:
	#输入用户名
	user_name = raw_input('please input user name:')
	#判断用户名在列表中
	if user_name in users.keys():
		while True:
			#若存在则输入密码
			passwd = raw_input('please input password:')
			#判断密码是否正确
			if users[user_name] == passwd:
				#密码正确，跳出
				print 'successful'
				flag = True
				break			
			#密码错误，判断三次
			else:
				print 'wrong password'
				i += 1
				if i == 3 :
					print 'this user locked'
					#更改用户状态
					user_stat.update({user_name:0})
					flag = True
					break
		if flag:
			break
	else:
		print 'wrong user name'
