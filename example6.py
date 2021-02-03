# -*- coding: utf-8 -*-
# @Time : 2021/2/3 0003
# @Author : yang
# @Email : 2635681517@qq.com
# @File : example6.py
from redis_db import con

"""用pipline传递批处理命令和执行事务"""
try:
    pipline = con.pipeline()
    pipline.watch("9856")
    # 开启事务
    pipline.multi()
    pipline.hset("9856", "name", "jack")
    pipline.hset("9856", "age", 35)
    pipline.execute()
    """关闭pipline()"""

except Exception as e:
    if "pipline" in dir():
        pipline.reset()
    print(e)
finally:
    del con
