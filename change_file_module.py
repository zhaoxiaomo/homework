#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json
import os
#打开文件，找到代码块，拿出来
def fetch(backend):
    fetch_list = []
    with open('ha') as obj:
        flag = False
        #obj.readlines()  #读取所有的行，放入列表
        for line in obj:
            if line.strip() == 'backend {backend}'.format(backend=backend):
                flag = True
                continue
            if flag and line.strip().startswith('backend'):
                break            #判断，如果是backend开头，不再放
            if flag and line.strip():
                fetch_list.append(line.strip())
    return fetch_list

def add1(dic_info):
    backend_title = dic_info.get('backend')  #从字典中获取backend的title
    crrent_title = 'backend {backend}'.format(backend=backend_title)     #记录的title
    crrent_record = "server {server} {server} weight {weight} maxconn {maxconn}".format(**data_dict.get('record'))   #记录的内容
    fetch_list = fetch(backend_title)           #匹配是否有backend记录
    if fetch_list:#存在backend，只需要再添加记录
        if crrent_record in fetch_list:
            pass
        else:
            fetch_list.append(crrent_record)
        #读配置文件，写入到新的配置文件中
        #读上 —— 新上
        #新处理完之后的配置文件写入到新配置文件中，fetch_list
        #读下 —— 新下
        flag = False
        has_write = False
        with open('ha','r') as read_obj,open('ha.new','w') as write_obj:   #fecth_list处理完之后，中间部分
            for line in read_obj:
                if line.strip() == crrent_title:
                    flag = True
                    write_obj.write(line)    #将backend写入到新配置文件里
                    continue
                if flag and line.strip().startswith('backend'):
                    # 判断，如果是backend开头，不再放
                    flag = False
                if flag:
                    if not has_write:
                        for new_line in fetch_list:
                            temp = "%s%s\n" % (" "*8, new_line)
                            write_obj.write(temp)  #把处理完的fetch_list写入新配置文件
                        has_write = True
                else:                    write_obj.write(line)
    else:#不存在backend记录，添加backend和记录
        with open('ha','r') as read_obj, open('ha.new','w') as write_obj:
            for line in read_obj:  #把原配置文件中的内容，写入到新的配置文件中
                write_obj.write(line)
            write_obj.write('\n'+crrent_title+'\n')
            temp = '%s%s\n'%(' '*8, crrent_record)
            write_obj.write(temp)
    os.rename('ha', 'ha.bak')
    os.rename('ha.new', 'ha')

s ='{"backend": "www.oldboy.org","record":{ "server": "100.1.1.11","weight": 30,"maxconn": 30}}'
data_dict = json.loads(s)
add1(data_dict)