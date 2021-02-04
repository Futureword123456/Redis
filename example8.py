# -*- coding: utf-8 -*-
# @Time : 2021/2/3 0003
# @Author : yang
# @Email : 2635681517@qq.com
# @File : example8.py
import random

from redis_db import con

try:
    con.delete("ballot")
    con.zadd('ballot', {"马云":0, "赵长岩": 0, "马化腾":0, "李彦宏": 0,"长江大学":0})

    names = ["马云", "赵长岩", "马化腾", "李彦宏", "长江大学"]
    for i in range(0, 300):
        num = random.randint(0, 4)
        name = names[num]
        con.zincrby("ballot", 1, name)
    result = con.zrevrange("ballot", 0, -1, "WITHSCORES")
    for one in result:
        print(one[0].decode('utf-8'), int(one[1]))
except Exception as e:
    print(e)
finally:
    del con
