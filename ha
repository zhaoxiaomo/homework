backend www.baidu.com
        server 1.1.1.1 1.1.1.1 weight 20 maxconn 20
        server 1.1.1.2 1.1.1.2 weight 20 maxconn 20
backend www.sina.com
        server 119.114.114.111 119.114.114.111 weight 20 maxconn 30
        server 119.114.114.112 119.114.114.112 weight 20 maxconn 30
backend www.oldboy.org
        server 100.1.1.9 100.1.1.9 weight 20 maxconn 30
        server 100.1.1.11 100.1.1.11 weight 30 maxconn 30
