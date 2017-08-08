#!/usr/env/python
# -*- coding:utf-8 -*-

dic = {
    'c':['asd|123|1','fwe|32|1']
}

def search(backend):
    search_list = []
    with open('fileopration.txt','r') as fileopen:
        flag = False
        for line in fileopen:
            #匹配到指定行
            if line.strip() == 'backend {backend}'.format(backend=backend):
                flag = True
                continue
            #已匹配，并且到一行为backend
            if flag and line.strip().startswith('backend'):
                break
            #已匹配，并且不为空行
            if flag and line.strip():
                search_list.append(line.strip())
    return search_list

def add():
    pass

def delete():
    pass

search('buy.oldboy.org')
