# -*- coding: utf-8 -*-
# @Time : 2021/2/3 0003
# @Author : yang
# @Email : 2635681517@qq.com
# @File : example5.py

"""redis的hash应用"""
from redis_db import con

try:
    con.hmset("9856", {"name": "Scott", "sex": "male", "age": "35"})
    con.hset("9856", "city", "NIUYOK")
    con.hdel("9856", "age")
    """判断name是否在9856这个hash里面"""
    re = con.hexists("9856", "name")
    print(re)

    result = con.hgetall("9856")
    print(type(result))
    for one in result:
        print(one.decode('utf-8'))

except Exception as e:
    print(e)
finally:
    del con
