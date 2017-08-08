#!/usr/env/python
# -*- coding:utf-8 -*-


import json
data = {"spam" : "foo", "parrot" : 42}
in_json = json.dumps(data)

import json
dic = {"a":1,"b":3}

data_dict ={"backend": "www.oldboy.org",
        "record":{
            "server": "100.1.1.9",
            "weight": 20,
            "maxconn": 30
        }}

jaso = json.dumps(data_dict)
print jaso