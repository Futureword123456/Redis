# -*- coding: utf-8 -*-
# @Time : 2021/2/3 0003
# @Author : yang
# @Email : 2635681517@qq.com
# @File : example2.py

from redis_db import con
"""mset、mget函数的使用"""
try:
    """删除记录"""
    con.delete("country", "city")
    """设置数据mset()参数用字典"""
    con.mset({"country": "德国", "city": "柏林"})
    rest = con.mget("country", "city")
    for one in rest:
        print(one.decode('utf-8'),end="|")

except Exception as e:
    print(e)
