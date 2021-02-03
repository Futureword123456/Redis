# -*- coding: utf-8 -*-
# @Time : 2021/2/3 0003
# @Author : yang
# @Email : 2635681517@qq.com
# @File : example4.py
"""集合的操作"""
from redis_db import con

try:
    """创建集合"""
    con.sadd("employee", 8001, 8002, 8003)
    """集合的删除"""
    con.srem("employee", 8002)
    """得到剩下的集合"""
    result = con.smembers("employee")
    for one in result:
        print(one.decode('utf-8'))

    """有序集合的创建"""
    con.zadd('keyword', {"马云","1.1"})
    # con.zadd("keyword","马云",0.2,"鹿晗",2.3)

    """增加10分"""
    con.zincrby("keyword", "10", "name1")
    result = con.zrevrange("keyword", 0, -1)
    for i in result:
        print(i.decode('utf-8'))

except Exception as e:
    print(e)
finally:
    del con
