# -*- coding: utf-8 -*-
import sqlite3

conn = sqlite3.connect('weather.db')
cur = conn.cursor()
try:
    cur.execute(
        'CREATE TABLE weather_day(prov varchar(16),city varchar(16) PRIMARY KEY,\
        year smallint,month smallint,day smallint,weather varchar(16),\
        wind varchar (32),highest_temp smallint)'
    )
except:
    print 'TABLE weather exists.'
    pass

cur.execute(
    "INSERT INTO weather_day(prov,city,year,month,day,weather,wind,highest_temp) \
    VALUES(%s,%s,%d,%d,%d,%s,%s,%d)" % (
        u"'上海'",
        u"'上海'",
        2016, 7, 25,
        "'sunny'", "'se 3-4'", 36))

#cur.execute("DELETE FROM weather_day WHERE highest_temp=36")

conn.commit()
cur.execute('select * from weather_day')
result = cur.fetchall()
for r in result:
    print r

cur.close()
conn.close()
