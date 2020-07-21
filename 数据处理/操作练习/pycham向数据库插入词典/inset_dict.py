import pymysql
import re
# create table words (id int primary key auto_increment,word varchar(50),mean varchar(800));
db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     password="123456",
                     database="dict",
                     charset="utf8")
cur = db.cursor()
f = open("dict.txt")
args_list=[]
sql="insert into words (word,mean) values (%s,%s);"
try:
    for line in f:
        print(line)
        l=re.findall(r"(\w+)\s+(.*)",line)
        print(l)
        args_list.append(l[0])
    cur.executemany(sql,args_list)
    db.commit()
except Exception as e:
    print(e)
    db.rollback()

f.close()
cur.close()
db.close()



