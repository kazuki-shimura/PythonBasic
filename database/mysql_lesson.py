#　mysql.pyで作成ファイルを作成しようとするとエラーが出る。


import mysql.connector

# conn = mysql.connector.connect(
#     host='127.0.0.1', user='root', password='Root/root8'
# )
#
# curs = conn.cursor()
#
# curs.execute(
#     'create database test_mysql_database'
# )
#
# curs.close()
# conn.close()

conn = mysql.connector.connect(
    host='127.0.0.1', user='root',
    password='Root/root8', database='test_mysql_database'
)

curs = conn.cursor()
# curs.execute( 'create table persons('
#              'id int not null auto_increment,'
#              'name varchar(14) not null,'
#              'primary key(id))')

# curs.execute('insert into persons(name) values("Mike")')
# conn.commit()

curs.execute('select * from persons')
for row in curs:
    print(row)

# curs.execute('update persons set name = "Michel" where id = "3"')
# conn.commit()

curs.execute('delete from persons where id = "4"')
conn.commit()


curs.close()
conn.close()


