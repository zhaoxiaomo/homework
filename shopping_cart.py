# -*- coding:utf-8 -*-

supermarket = {'imac':6666,
               'iphone':5888,
               'ipad':2999,
               'watch':399}

shop_list = []
# 读入钱数
start = file('I:\item\homework\day2\wallet.py', 'r')
# 将钱数赋值
money = int(start.read())
start.close()

while True:
    #打印购物清单
    print '\033[1;26mGOODS\033[0m'
    for k in supermarket.keys():print k + '\t' + str(supermarket[k])
    print '\033[1;33mInput [q | quit] to quit\033[0m'
    #输入想要购买的物品
    buy = raw_input('please input what you want buy:')
    #判断购买物品是否在商品中
    if buy in supermarket.keys():
        #如果在，将钱数和商品进行对比
        buy_m = supermarket[buy]
        if money > buy_m :
            #如果钱数>商品，则扣除钱数，显示购买成功，请继续挑选
            money = money - buy_m
            print 'success……当前余额：' + str(money)
            shop_list.append(buy)
            continue
        if money < buy_m:
            print 'no enough money'
            continue
    elif buy == 'q' or buy == 'quit':
        break
    #如果不在，显示该商品不存在
    else:
        print '\033[1;36mthis good not in GOODS\033[0m'
        continue

print '\nThe shop list:'
print '\n'.join(shop_list)
print '余额 : ' +str(money)

stop = file('I:\item\homework\day2\wallet.py','w')
a = str(money)
stop.write(a)
stop.flush()
stop.close()

