import pymysql

db=pymysql.connect(host="localhost",
                   port=3306,
                   user="root",
                   password="123456",
                   database="save_file",
                   charset="utf8")
cur=db.cursor()
# f=open("王者荣耀启动.jpeg","rb")
# msg=f.read()
# target_mag=[(msg)]
# print(target_mag)
# sql="insert into sf (content) values (%s);"
# try:
#     cur.execute(sql,msg)
#     db.commit()
# except Exception as e:
#     print(e)
#     print("出错了")

f=open("get.jpg","wb")
sql="select content from sf where id=1;"
cur.execute(sql)
get_msg=cur.fetchone()
f.write(get_msg[0])
f.close()
cur.close()
db.close()



