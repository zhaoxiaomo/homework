#!/usr/bin/env python
# -*- coding:utf-8 -*-

china = ['beijing', 'shanghai', 'guangzhou']
hanguo = ['shouer']
riben = ['dongjing']
yingguo = ['lundun']
faguo = ['bali']
deguo = ['munihei']

asia = ['china', 'hanguo', 'riben']
europe = ['yingguo', 'faguo', 'deguo']
america = ['meiguo']

zhou = ['asia', 'europe', 'america']

def country(arg):
	switcher = {
		'asia':asia,
		'europe':europe,
		'america':america
	}
	return switcher.get(arg)

def city(arg):
	switcher = {
		'china':china,
		'hanguo':hanguo,
		'riben':riben
	}
	return switcher.get(arg)

flag = False
while True:
	#将洲赋值给zz
	zz = raw_input('[' + ','.join(zhou) + ']\nqing shu ru zhou:')
	if zz in zhou:
		while True:
			#显示洲所包含的国家
			print country(zz)
			#将国家赋值给gg
			gg = raw_input('please input the country:')
			if gg in country(zz):
				print city(gg)
				flag = True
				break
			elif gg == 'back':
				break
			else:
				print "don't have this country"
		if flag:
			break
	else:
		print "don't have this zhou"
