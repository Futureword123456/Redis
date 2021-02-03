# -*- coding: utf-8 -*-
# @Time : 2021/2/3 0003
# @Author : yang
# @Email : 2635681517@qq.com
# @File : example3.py
"""列表的基本操作"""
from redis_db import con

try:
    """创建列表"""
    con.rpush("dname", "董事会", "秘书处", "财务部", "技术部")
    """删除第一个列表"""
    con.lpop("dname")
    """得到剩下的课本元素"""
    result = con.lrange("dname", 0, 1)
    for one in result:
        print(one.decode('utf-8'))
except Exception as e:
    print(e)

finally:
    del con
