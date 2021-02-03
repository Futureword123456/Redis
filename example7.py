# -*- coding: utf-8 -*-
# @Time : 2021/2/3 0003
# @Author : yang
# @Email : 2635681517@qq.com
# @File : example7.py
from redis_db import con

try:
    file = open(file="redis1.txt", mode="r", encoding='utf-8')
    data = file.read().splitlines()
    print(data)
    for one in data:
        temp = one.split(",")
        print(temp)
        sid = temp[0]
        name = temp[1]
        classno = temp[2]
        score_1 = int(temp[3])
        score_2 = int(temp[4])
        score_3 = int(temp[5])
        if score_1 >= 85 and score_2 >= 85 and score_3 >= 85:
            con.hmset(sid, {"name": name, "classno": classno,
                            "score_1": score_1,
                            "score_2": score_2,
                            "score_3": score_3})

        print("没有三科成绩都大于等于{0}分的学生".format(85))

except Exception as e:
    print(e)
finally:
    if "file" in dir():
        file.close()
    del con
