#coding: utf-8
import redis
from random import randint


r = redis.Redis(host = 'localhost', port = 6379, db = 0)
for x in range(100):
    #=.=就随便设置一个65535的上界来随机了
    r.set(x, randint(0,65535))
r.save()

#测试：
for n in range(100):
    print(r.get(n)),