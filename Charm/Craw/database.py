import MySQLdb

conn = MySQLdb.connect(host='localhost', user='root', passwd='314', port=3306)
cur = conn.cursor()
'''
try:
    cur.execute('create database if not exists book_db')
except MySQLdb.Error, e:
    print "Error %d: %s" % (e.args[0], e.args[1])
    '''
conn.select_db('book_db')
# cur.execute('create table book(id int,name varchar(64),author varchar(64),intro varchar(1024))')
value = [0, 'book1', 'xsj', 'haha']
# cur.execute('insert into book values(%s,%s,%s,%s)', value)
cur.execute('select * from book')
print cur.fetchone()
conn.commit()
cur.close()
conn.close()
