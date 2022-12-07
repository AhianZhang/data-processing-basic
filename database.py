import datetime
import os

import pymysql

host = "localhost"
user = "root"
passwd = "123456"
db = "demo"
table = "t_user"
field = "name,gender,address,create_time"

createTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(createTime)
try:
    conn = pymysql.connect(host=host, user=user, db=db, passwd=passwd)
    cursor = conn.cursor()
    print('数据库连接成功！')
    print(' ')
except:
    print('数据库连接失败！')
path = os.getcwd()
print(path)


# save
def insert():
    # sql = 'insert into {} ({}) values ({})'.format(table, field, "'ahian',1,'av','" + createTime+"'")
    affectRow = cursor.execute("insert into t_user (name, gender, address, create_time) VALUES (%s,%s,%s,%s)",
                               ('ahian', 1, 'av', createTime))
    print(affectRow)
    conn.commit()


#  query
def select_all():
    cursor.execute("select * from t_user")
    rows = cursor.fetchall()
    print(rows)


# query
def select_by_name(name):
    cursor.execute("select * from t_user where name = %s", name)
    rows = cursor.fetchone()  # 一个
    # rows = cursor.fetchmany(2) # 指定个数
    # rows = cursor.fetchall() # 全部
    print(rows)

# update
def update_by_id(name,id):
    cursor.execute("update t_user set name = %s where id = %s", (name,id))
    conn.commit()

if __name__ == '__main__':
    insert()
    select_all()
    select_by_name("ahian")
    update_by_id("zhangsan", 3)
