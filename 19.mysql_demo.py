import os
import MySQLdb #pip install mysqlclient
db = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd='Aa123456',
    db="test"
)
cur = db.cursor()
name = input('Enter name:')
print('您输入的用户name是：'.format(name))
password = input('Enter password:')
print('您输入的密码是：'.format(password))
#直接拼接sqL警数
sql = "SELECT * FROM user WHERE username='"+name+"'"+"AND password='"+password+"'"
# sql = "SELECT * FROM user WHERE username='"+name+"'"+"AND password=md5('"+password+"')"
print(sql)
cur.execute(sql)

# # 解决sql注入问题
# sql = "SELECT * FROM user WHERE username=%s AND password=%s"
# cur.execute(sql,(name,password))

for row in cur.fetchall():
    print(row)
db.close()

# 当 username=lisi'--'，--在sql中会被备注