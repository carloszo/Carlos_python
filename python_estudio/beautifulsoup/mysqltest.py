import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='a12345',
    db='wikiurl',
    charset='utf8'
)

try:
   with connection.cursor() as cursor:
        sql = 'insert into wikiurl(urlname,urlhref) values(%s,%s)'
        cursor.execute(sql,('name2','www.baidu.com'))
        connection.commit()
finally:
    connection.close()
