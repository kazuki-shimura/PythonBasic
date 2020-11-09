import sqlite3

# conn = sqlite3.connect('test_sqlite.db')
conn = sqlite3.connect(':memory:')

curs = conn.cursor()

curs.execute(
    'create table persons(id integer primary key autoincrement, name string)'
)
conn.commit()

curs.execute(
    'insert into persons(name) values("Mike")'
)
conn.commit()

curs.execute('select * from persons')
print(curs.fetchall())

curs.execute(
    'insert into persons(name) values("Nancy")'
)
curs.execute(
    'insert into persons(name) values("Tom")'
)
conn.commit()

curs.execute('update persons set name = "Michel" where name = "Mike"')

curs.execute(' delete from persons where name = "Michel" ')

conn.commit()
curs.execute('select * from persons')
print(curs.fetchall())

curs.close()
conn.close()