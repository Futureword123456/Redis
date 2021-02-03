# -*- coding: utf-8 -*-
# @Time : 2021/2/3 0003
# @Author : yang
# @Email : 2635681517@qq.com
# @File : example1.py


from redis_db import con
"""设置值key values"""
con.set("country", "英国")
con.set("city", "伦敦")
city = con.get("city").decode('utf-8')
con.expire("city", 5)

print(city)

"""链接归还"""
del con
