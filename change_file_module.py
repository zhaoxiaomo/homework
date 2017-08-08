#!/usr/bin/env python
# -*- coding:utf-8 -*-

#打开文件，找到代码块，拿出来
def fetch(backend):
    fetch_list = []
    with open('ha') as obj:
        flag = False
        #obj.readlines()  #读取所有的行，放入列表
        for line in obj:
            if line.strip() == 'backend {backend}'.format(backend):
                flag = True
                continue
            if flag and line.strip().startswith('backend'):
                break
            #判断，如果是backend开头，不再放
            if flag and line.strip():
                fetch_list.append(line.strip())
    return fetch_list

def add1(dic_info):
    backend_title = dic_info.get('backend')
    crrent_record = "server {server} {server} weight {weight} maxconn {maxconn}".format(**data_dict.get('record'))
    print crrent_record

data_dict ={"backend": "www.oldboy.org",
        "record":{
            "server": "100.1.1.9",
            "weight": 20,
            "maxconn": 30
        }}
#data_dict = json.loads(s)
#print data_dict

add1(data_dict)