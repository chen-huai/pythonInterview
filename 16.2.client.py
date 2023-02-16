# -*- coding: UTF-8 -*-
import os

# data = ['http://locahost:121/api',
#         'www.csdn.cn']
#
# for item in data:
#     tmpres = os.popen('curl %s' % item).readlines()
#     print(tmpres)
tmpres = os.popen('curl http://locahost:121/api')
print(tmpres.name)
print(tmpres)

print("ok..")